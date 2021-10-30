 //------- MAGNIFICENT POPUP ---//

      $(document).ready(function() {

        "use strict";

          $('.image-modal').magnificPopup({

          type:'inline',
          fixedContentPos: false,
          removalDelay: 100,
          closeBtnInside: true,
          preloader: false,
          mainClass: 'mfp-fade'

          });

          $(document).on('click', '.popup-modal-dismiss', function (e) {
          e.preventDefault();
          $.magnificPopup.close();
          });


        $('.image-popup-no-margins').magnificPopup({
          type: 'image',
          closeOnContentClick: true,
          closeBtnInside: false,
          fixedContentPos: true,
          mainClass: 'mfp-no-margins mfp-with-zoom', // class to remove default margin from left and right side
          image: {
            verticalFit: true
          },
          zoom: {
            enabled: true,
            duration: 300 // don't foget to change the duration also in CSS
          }
        });

        $('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
          disableOn: 700,
          type: 'iframe',
          mainClass: 'mfp-fade',
          removalDelay: 160,
          preloader: false,

          fixedContentPos: false
        });

      });



//------- SITE LOADER ---//

jQuery(window).load(function() { 
    jQuery("#loaderInner").fadeOut(); 
    jQuery("#loader").delay(400).fadeOut("slow"); 


});

//------- ACTIVE LINKS SCROLLSPY ---//

$('body').scrollspy({ offset: 200, target: '.navigation' });



// HEADER SCROLL EFFECT

jQuery(document).ready(function($){ 
    $( window ).scroll(function() {
      var heights = window.innerHeight;
      document.getElementById("sectionIntro").style.height = heights * 0.8 + "px";


    });

});


jQuery(document).ready(function($){
var introSection = $('#sHomeBg'),
    introSectionHeight = introSection.height(),

    //change opacitySpeed if you want to change the speed of opacity reduction effect
    opacitySpeed = 1.2; 

triggerAnimation();
$(window).on('resize', function(){
    triggerAnimation();
});

//bind the scale event to window scroll if window width > $MQ (unbind it otherwise)
function triggerAnimation(){
        $(window).on('scroll', function(){
            //The window.requestAnimationFrame() method tells the browser that you wish to perform an animation- the browser can optimize it so animations will be smoother
            window.requestAnimationFrame(animateIntro);
        });
}
//assign a scale transformation to the introSection element and reduce its opacity
function animateIntro () {
    var scrollPercentage = ($(window).scrollTop()/introSectionHeight).toFixed(5);
    //check if the introSection is still visible
    if( $(window).scrollTop() < introSectionHeight) {
        introSection.css({
            'opacity': 1 - scrollPercentage*opacitySpeed
        });
    }
}

});