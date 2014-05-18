/*global jQuery */

;(function($) {
	$(function() {
		$('#organize-button').bind('click', function(e) {
			$('#organize-popup-1').bPopup({
				contentContainer:'#popup-content-1',
				loadUrl: '/static/incs/organize.html',
<<<<<<< HEAD
=======
				position: [150, 150]
>>>>>>> 5546f99237fcc1916c625a1be0614e4b40e266a0
			}, function () {
				$('li', '#choices-list').on('click', function(e) {
					$('#organize-popup-1').bPopup().close()
					$('#organize-popup-2').bPopup({
						contentContainer:'#popup-content-2',
						loadUrl: '/offers/list',
<<<<<<< HEAD
=======
						position: [150, 150],
>>>>>>> 5546f99237fcc1916c625a1be0614e4b40e266a0
						loadCallback: function () {
							$('#create-event-bttn').attr("disabled", "disabled");
							$('li.offer').on('click', function (e) {
								$(this).addClass('active');
								$(this).siblings().removeClass('active');
								$('#create-event-bttn').removeAttr("disabled");
								$.cookie('selected_offer',
									$(this).data('offer-id'));
							});
							$('#create-event-bttn').on('click', function (e) {
								top.location.href = "/events/create/"
									+ $.cookie('selected_offer');	
							});
						}
					});
				});
			});
		});
	});
})(jQuery);
