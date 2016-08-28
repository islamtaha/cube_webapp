	$(document).ready(function() {
	  $('#carousel').waltzer({
	    vertical: true, // enable vertical scrolling
	    offset: 0, // Item to start on, items will be reordered positioning the specified item first.
	    circular: false, // Circular or linear scrolling.
	    auto: true, // autoplay on load
	    autoPause : 3000, // Pause time between each automatic transition, when autoplay is enabled.
	    speed: 600, // Time to complete each transition.
	    easing: 'swing', // easing options. Requires jQuery easing plugin or jQuery UI.
	    navBtns: true, // arrows navigation
		scroll:1,

	  });
	});

