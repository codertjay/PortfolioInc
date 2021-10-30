
(function($) {
    "use strict";
     $(document).on('ready', function() {	
	
		
		/*====================================
			Header Sticky JS
		======================================*/ 
		jQuery(window).on('scroll', function() {
			if ($(this).scrollTop() > 200) {
				$('.header').addClass("sticky");
			} else {
				$('.header').removeClass("sticky");
			}
		});
		/*====================================
			Mobile Menu JS
		======================================*/ 
		$('.mobile-menu').slicknav({
			prependTo:".mobile-nav",
			label: '',
			duration: 500,
			easingOpen: "easeOutBounce",
		});
		
		/*================================
			Hero Slider
		================.==================*/ 
		$('.hero-slider').owlCarousel({
			items:1,
			autoplay:true,
			loop:true,
			autoplayTimeout:4000,
			autoplayHoverPause:false,
			smartSpeed: 700,
			merge:true,
			nav:false,
			dots:true,
		});	
		
		/*================================
			Blog Slider
		==================================*/ 
		$('.blog-slider').owlCarousel({
			items:3,
			autoplay:true,
			loop:true,
			margin:30,
			autoplayTimeout:3500,
			autoplayHoverPause:false,
			smartSpeed: 600,
			merge:true,
			nav:true,
			navText: ['<i class="fa fa-angle-left" aria-hidden="true"></i>', '<i class="fa fa-angle-right" aria-hidden="true"></i>'],
			dots:false,
			responsive:{
				300: {
					items:1,
				},
				480: {
					items:1,
				},
				768: {
					items:2,
				},
				1170: {
					items:3,
				},
			}
		});		
		
		/*================================
			Testimonial JS
		==================================*/ 
		$('.testimnial-slider').owlCarousel({
			items:1,
			autoplay:true,
			loop:true,
			autoplayTimeout:3500,
			autoplayHoverPause:false,
			smartSpeed: 600,
			merge:true,
			nav:false,
			dots:true,
		});	
		
		$('#portfolio-item').cubeportfolio({
			filters: '#portfolio-nav',
			loadMoreAction: 'click',
			defaultFilter: '*',
			layoutMode: 'grid',
			animationType: 'quicksand',
			gridAdjustment: 'responsive',
			gapHorizontal: 30,
			gapVertical: 30,
			mediaQueries: [{
				width: 1100,
				cols: 3,
			},{
				width: 768,
				cols: 3,
			}, {
				width: 480,
				cols: 2,
			},{
				width: 0,
				cols: 1,
			}],
			caption: 'overlayBottomPush',
			displayType: 'sequentially',
			displayTypeSpeed: 80,


		});
		
		/*================================
			Client Slider
		==================================*/ 
		$('.client-slider').owlCarousel({
			items:4,
			autoplay:true,
			loop:true,
			margin:15,
			autoplayTimeout:4000,
			autoplayHoverPause:false,
			smartSpeed: 1000,
			merge:true,
			nav:true,
			navText: ['<i class="fa fa-angle-left" aria-hidden="true"></i>', '<i class="fa fa-angle-right" aria-hidden="true"></i>'],
			dots:false,
			responsive:{
				300: {
					items:2,
				},
				480: {
					items:2,
				},
				768: {
					items:3,
				},
				1170: {
					items:4,
				},
			}
		});		
		
		/*=====================================
			Video Popup
		======================================*/ 
		$('.video-popup').magnificPopup({
			type: 'iframe',
			removalDelay: 300,
			mainClass: 'mfp-fade'
		});
		
		/*====================================
		//  Parallax JS
		======================================*/ 
		 $(window).stellar({
            responsive: true,
            positionProperty: 'position',
            horizontalScrolling: false
        });
		
		/*====================================
			Counter Js
		======================================*/ 
		$('.counter').counterUp({
			time: 1000
		});
		
		/*====================================
			Wow JS
		======================================*/		
		var window_width = $(window).width();   
			if(window_width > 767){
            new WOW().init();
		}
		
		/*================================
			ScrollUp JS
		==================================*/
		$.scrollUp({
			scrollName: 'scrollUp',      // Element ID
			scrollDistance: 500,         // Distance from top/bottom before showing element (px)
			scrollFrom: 'top',           // 'top' or 'bottom'
			scrollSpeed: 1000,            // Speed back to top (ms)
			animation: 'fade',           // Fade, slide, none
			animationSpeed: 50,         // Animation speed (ms)
			scrollTrigger: false,        // Set a custom triggering element. Can be an HTML string or jQuery object
			scrollTarget: false,         // Set a custom target element for scrolling to. Can be element or number
			easing: 'easeInOut',
			scrollText: ["<i class='fa fa-angle-up'></i>"], // Text for element, can contain HTML
			scrollTitle: false,          // Set a custom <a> title if required.
			scrollImg: false,            // Set true to use image
			activeOverlay: false,        // Set CSS color to display scrollUp active point, e.g '#00FFFF'
			zIndex: 2147483647           // Z-Index for the overlay
		});		
		
		$('.p-anim-btn').on('click', function(event) {
			var $anchor = $(this);
			$('html, body').stop().animate({
				scrollTop: $($anchor.attr('href')).offset().top - 80 
			}, 1000, 'easeInOutQuart');
			event.preventDefault();
		});
	});
	
	/*================================
			Preloader JS
	==================================*/
	 var prealoaderOption = $(window);
      prealoaderOption.on("load", function () {
          var preloader = jQuery('.sk-cube-grid');
          var preloaderArea = jQuery('.preloader-area');
          preloader.fadeOut();
          preloaderArea.delay(350).fadeOut('slow');
      });

})(jQuery);