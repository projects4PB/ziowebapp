/*global jQuery */

;(function($) {
	$(function() {
		var directionsDisplay;
		var directionsService;
		var map;
		var poland;
		function mapa()
		{
			var rendererOptions = {
					draggable : true
				};
				directionsDisplay = new google.maps.DirectionsRenderer(rendererOptions);
				
				directionsService = new google.maps.DirectionsService();

				poland = new google.maps.LatLng(52.274398, 19.775136);
		}

		function initialize() {
			var mapOptions = {
				zoom : 7,
				center : poland
			};
			map = new google.maps.Map(document.getElementById('map-canvas'),
					mapOptions);
			directionsDisplay.setMap(map);
			directionsDisplay.setPanel(document.getElementById('directionsPanel'));

			google.maps.event.addListener(directionsDisplay, 'directions_changed',
					function() {
						computeTotalDistance(directionsDisplay.getDirections());
					});		
		}

		function calcRoute() {
			var request = {
				origin : document.getElementById('road-from').value,
				destination : document.getElementById('road-to').value,
				
				travelMode : google.maps.TravelMode.DRIVING
			};
			directionsService.route(request, function(response, status) {
				if (status == google.maps.DirectionsStatus.OK) {
					directionsDisplay.setDirections(response);
				}
			});
		}

		function computeTotalDistance(result) {
			var total = 0;
			var cenaPaliwa = document.getElementById('cenaPaliwa').value;
			var spalanie = document.getElementById('spalanie').value;
			var paliwo;
			var koszt;
			var myroute = result.routes[0];
			for (var i = 0; i < myroute.legs.length; i++) {
				total += myroute.legs[i].distance.value;
			}
			total = total / 1000.0;
			paliwo=total/100.0*spalanie;
			paliwo=Math.round( paliwo * 100 ) / 100;
			koszt=paliwo*cenaPaliwa;
			document.getElementById('total').innerHTML ='dystans:' + total
				+ ' km, paliwo: ' + paliwo + ' l, koszt: ' +koszt + ' zl';
		}
		mapa();
		if($('#road-from').val() != undefined & $('#road-to').val() != undefined) {
			initialize();
			calcRoute();
		}
		$('#calc-button').click(function (e) {
			initialize();
			calcRoute();
		});
		$('#post-comment-bttn').click(function (e) {
			if(!$('#id_comment').val()) {
				e.preventDefault();
			}
		});
		$('.vote-link').click(function (e) {
			$.ajax('/places/rate/' + $(this).data('obj-id') + '/'
				+ $(this).data('vote') + '/', {
					csrfmiddlewaretoken: $.cookie('csrftoken'),
					statusCode: {
						403: function (data) {
							$('#voting-messages').text('Oddałeś już głos na ten obiekt');
						},
						200: function (data) {
							$('#voting-messages').text('Twoja ocena została zapisana w bazie');
							$('#vote-choices').hide();
						}
					}
				});
		});
		$('.image-popup').click(function (e) {
			$('#image-popup').bPopup({
				content: 'image',
				contentContainer: '#image-content',
				loadUrl: $(this).data('image-url')
			});
		});
		$('.organize-popup').hide()
		$('#organize-button').bind('click', function(e) {
			$('#organize-popup-1').bPopup({
				contentContainer:'#popup-content-1',
				loadUrl: '/static/incs/organize.html',
			}, function () {
				$('li', '#choices-list').on('click', function(e) {
					$.cookie('selected_type', $(this).data('trip-type'));
					$('#organize-popup-1').bPopup().close()
					$('#organize-popup-2').bPopup({
						contentContainer:'#popup-content-2',
						loadUrl: '/choices/offers-list/' + $.cookie('selected_type'),
						loadCallback: function () {
							$('#create-event-bttn').attr("disabled", "disabled");
							$('#plan-road-bttn').attr("disabled", "disabled");
							$('li.offer').on('click', function (e) {
								$(this).addClass('active');
								$(this).siblings().removeClass('active');
								$('#create-event-bttn').removeAttr("disabled");
								$('#plan-road-bttn').removeAttr('disabled');
								$.cookie('selected_offer',
									$(this).data('offer-id'));
							});
							$('#create-event-bttn').on('click', function (e) {
								top.location.href = "/events/create/"
									+ $.cookie('selected_offer');	
							});
							$('#search-field').keyup(function (e) {
								$.post('search/' + $.cookie('selected_type') + '/', {
									phrase: $(this).val(),
									csrfmiddlewaretoken: $.cookie('csrftoken') 
								}, function(data) {
									$('div#offers-list').html(data);
									$('li.offer').on('click', function (e) {
										$(this).addClass('active');
										$(this).siblings().removeClass('active');
										$('#create-event-bttn').removeAttr("disabled");
										$('#plan-road-bttn').removeAttr('disabled');
										$.cookie('selected_offer',
											$(this).data('offer-id'));
									});
								});
							});
							$('.tourist-obj-link').click(function (e) {
								var touristObjPK = $(this).data('tourist-obj-pk');
								$('#organize-popup-3').bPopup({
									contentContainer:'#popup-content-3',
									loadUrl: '/places/detail-ajax/' + touristObjPK + '/',
									loadCallback: function () {}
								});
							});
							$('#plan-road-bttn').on('click', function (e) {
								$('#organize-popup-2').bPopup().close()
								top.location.href = "/places/road/"
									+ $.cookie('selected_offer');	
							});
						}
					});
				});
			});
		});
	});
})(jQuery);
