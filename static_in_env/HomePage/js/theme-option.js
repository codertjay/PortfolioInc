(function($) {
    "use strict";
    $(document).on('ready', function() {	
	
		/* Bonik Settings */
		$('.elena-options .icon').on('click', function(event){
			event.preventDefault();
			if( $ (this).hasClass('inOut')  ){
				$('.elena-options').stop().animate({right:'0px'},500 );
			} else{
				$('.elena-options').stop().animate({right:'-245px'},500 );
			} 
			$(this).toggleClass('inOut');
			return false;

		});

		/* Bonik Colors */
		$(".skin1" ).on('click', function(){
			$("#bonik_custom" ).attr("href", "css/colors/color1.css" );
			return false;
		});
		$(".skin2" ).on('click', function(){
			$("#bonik_custom" ).attr("href", "css/colors/color2.css" );
			return false;
		});
		$(".skin3" ).on('click', function(){
			$("#bonik_custom" ).attr("href", "css/colors/color3.css" );
			return false;
		});
		$(".skin4" ).on('click', function(){
			$("#bonik_custom" ).attr("href", "css/colors/color4.css" );
			return false;
		});
		$(".skin5" ).on('click', function(){
			$("#bonik_custom" ).attr("href", "css/colors/color5.css" );
			return false;
		});
		$(".skin6" ).on('click', function(){
			$("#bonik_custom" ).attr("href", "css/colors/color6.css" );
			return false;
		});
		$(".skin7" ).on('click', function(){
			$("#bonik_custom" ).attr("href", "css/colors/color7.css" );
			return false;
		});
		$(".skin8" ).on('click', function(){
			$("#bonik_custom" ).attr("href", "css/colors/color8.css" );
			return false;
		});
	});	
		
})(jQuery);