/*global jQuery */

;(function($) {
	$(function() {
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
							$('#plan-road-bttn').on('click', function (e) {
								$('#organize-popup-2').bPopup().close()
								$('#organize-popup-3').bPopup({
									contentContainer:'#popup-content-3',
									loadUrl: '/static/incs/plan_road.html',
									loadCallback: function () {
										console.log("trasa");
										var wspolrzedne = new google.maps.LatLng(53.41935400090768,14.58160400390625);
										    var opcjeMapy = {
												      zoom: 10,
									      center: wspolrzedne,
									      mapTypeId: google.maps.MapTypeId.ROADMAP
									    };
											    var mapa = new google.maps.Map(document.getElementById("google-map"), opcjeMapy); 
									}
								});
							});
						}
					});
				});
			});
		});
	});
})(jQuery);
