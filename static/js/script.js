$(function() {
  $('a[href*=#]:not([href=#])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top
        }, 1000);
        return false;
      }
    }
  });
})


$(document).ready(function() {
  $('#carousel').waltzer({
                scroll:1,
                navBtns: false,
                pager:true,
                auto:true,
                autoPause: 4000,
                circular: true, // Circular or linear scrolling.
                speed: 500, // Time to complete each transition.

                 // autoPause : 10, // Pause time between each automatic transition, when autoplay is enabled.
    // vertical: false, // enable vertical scrolling
    // scroll: 3, // Number of items to scroll during each transition.
    // offset: 0, // Item to start on, items will be reordered positioning the specified item first.
    // auto: true, // autoplay on load
    // easing: 'swing', // easing options. Requires jQuery easing plugin or jQuery UI.
    // navBtns: true, // arrows navigation
    // leftNavBtn: 'left-nav-btn', // Class name for the 'previous' button 
    // rightNavBtn: 'right-nav-btn', // Class name for the 'next' button 
    // pager: true, // pager navigation
    // onCreate: null, // callback function
    // onComplete: null, // callback function
    // onForwardComplete: null, // callback function
    // onBackwardComplete: null // callback function
  });
});


$("a[href^=#]").on("click", function(e) {
  e.preventDefault();
  history.pushState({}, "", this.href);
});




$(document).ready(function(){
  var hash = document.URL.split("#")[1];
    // alert(hash);
    var elementID = "#"+hash+"_link"
    $(elementID).addClass("active"); 
    $(".sec_icon").click(function(){
      $(".sec_icon").removeClass("active");
      $(this).addClass("active");
    });

    new WOW().init();

    $('#test1').gmap3({
      map:{
        options:{
          center:[31.037630,31.355597],
          zoom:16
        }
      },
      marker:{
        values:[
        {latLng:[31.037630,31.355597], data:"Welcome To CUBE !"},
        ],
        options:{
          draggable: false,
          icon: "img/cube_icon .png"
        },
        events:{
          mouseover: function(marker, event, context){
            var map = $(this).gmap3("get"),
            infowindow = $(this).gmap3({get:{name:"infowindow"}});
            if (infowindow){
              infowindow.open(map, marker);
              infowindow.setContent(context.data);
            } else {
              $(this).gmap3({
                infowindow:{
                  anchor:marker, 
                  options:{content: context.data}
                }
              });
            }
          },

          
          mouseout: function(){
            var infowindow = $(this).gmap3({get:{name:"infowindow"}});
            if (infowindow){
              infowindow.close();
            }
          }
        }
      }
    });
});
