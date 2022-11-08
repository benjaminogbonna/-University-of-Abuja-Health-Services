(function($) {
	'use strict';

	/*====================
	MEAN MENU JS
	======================*/
	$('.mean-menu').meanmenu({ 
		meanScreenWidth: "991"
	});

	/*====================
	PRELOADER JS
	======================*/
	$(window).on('load', function() {
		$('.preloader').fadeOut();
	});

	/*====================
	NICE SELECT JS
	======================*/
	$('select').niceSelect();
	
	/*====================
	HEADER STICKY JS
	======================*/
	$(window).on('scroll', function() {
		if ($(this).scrollTop() >150){  
			$('.navbar-area').addClass("is-sticky");
		}
		else{
			$('.navbar-area').removeClass("is-sticky");
		}
	});

	/*====================
	HERO SLIDER WRAP JS
	======================*/
	$('.hero-slider-wrap').owlCarousel({
		loop:true,
		margin:0,
		nav:true,
		mouseDrag:true,
		items:1,
		dots:false,
		autoHeight:true,
		autoplay: true,
		smartSpeed:800,
		autoplayHoverPause:true,
		navText: [
			"<i class='bx bx-chevrons-left'></i>",
			"<i class='bx bx-chevrons-right'></i>"
		]
	});

	/*====================
	TESTIMONIAL WRAP JS
	======================*/
	$('.testimonial-wrap').owlCarousel({
		loop:true,
		margin:0,
		nav:false,
		mouseDrag:true,
		items:1,
		dots:true,
		autoHeight:true,
		autoplay:true,
		smartSpeed:1500,
		autoplayHoverPause:true,
		center:false,
		responsive:{
			0:{
				items:1,
				margin:10
			},
			576:{
				items:1,
				margin:10
			},
			768:{
				items:2,
				margin:20
			},
			992:{
				items:2
			},
			1200:{
				items:2
			}
		}
	});

	/*====================
	DEPARTMENT WRAP JS
	======================*/
	$('.department-wrap').owlCarousel({
		loop:true,
		margin:0,
		nav:false,
		mouseDrag:true,
		items:1,
		dots:true,
		autoHeight:true,
		autoplay:true,
		smartSpeed:1500,
		autoplayHoverPause:true,
		center:false,
		responsive:{
			0:{
				items:1,
				margin:10
			},
			576:{
				items:1,
				margin:10
			},
			768:{
				items:2,
				margin:20
			},
			992:{
				items:2
			},
			1200:{
				items:3
			}
		}
	});

	/*====================
	BLOG WRAP JS
	======================*/
	$('.blog-wrap').owlCarousel({
		loop:true,
		margin:0,
		nav:false,
		mouseDrag:true,
		items:1,
		dots:true,
		autoHeight:true,
		autoplay:true,
		smartSpeed:1500,
		autoplayHoverPause:true,
		center:false,
		responsive:{
			0:{
				items:1,
				margin:10
			},
			576:{
				items:1,
				margin:10
			},
			768:{
				items:2,
				margin:20
			},
			992:{
				items:2
			},
			1200:{
				items:3
			}
		}
	});

	/*====================
	BLOG SIDEBAR JS
	======================*/
	$('.blog-sidebar-wrap').owlCarousel({
		loop:true,
		margin:0,
		nav:false,
		mouseDrag:true,
		items:1,
		dots:true,
		autoHeight:true,
		autoplay:true,
		smartSpeed:1500,
		autoplayHoverPause:true,
		center:false,
		responsive:{
			0:{
				items:1,
				margin:10
			},
			576:{
				items:1,
				margin:10
			},
			768:{
				items:2,
				margin:20
			},
			992:{
				items:2
			},
			1200:{
				items:2
			}
		}
	});

	/*====================
	TEAM WRAP JS
	======================*/
	$('.doctor-wrap').owlCarousel({
		loop:true,
		margin:0,
		nav:false,
		mouseDrag:true,
		items:1,
		dots:true,
		autoHeight:true,
		autoplay:true,
		smartSpeed:1500,
		autoplayHoverPause:true,
		center:false,
		responsive:{
			0:{
				items:1,
				margin:10,
			},
			576:{
				items:1,
				margin:10
			},
			768:{
				items:2,
				margin:20
			},
			992:{
				items:2
			},
			1200:{
				items:3
			}
		}
	});

	/*====================
	DATETIMEPICKER2 JS
	======================*/
	$('#datetimepicker2').datepicker({
		weekStart: 0,
		todayBtn: "linked",
		language: "es",
		orientation: "bottom auto",
		keyboardNavigation: false,
		autoclose: true
	});

	/*====================
	ODOMETER JS
	======================*/
	$('.odometer').appear(function(e) {
		var odo = $(".odometer");
		odo.each(function() {
			var countNumber = $(this).attr("data-count");
			$(this).html(countNumber);
		});
	});

	/*====================
	SCROLL JS
	======================*/
	$(window).on('scroll', function(){
		var scrolled = $(window).scrollTop();
		if (scrolled > 300) $('.go-top').addClass('active');
		if (scrolled < 300) $('.go-top').removeClass('active');
	});  

	/*====================
	GO-TOP JS
	======================*/
	$('.go-top').on('click', function() {
		$("html, body").animate({ scrollTop: "0" },  50);
	});

	/*====================
	FAQ JS
	======================*/
	$('.accordion').find('.accordion-title').on('click', function(){
		$(this).toggleClass('active');
		$(this).next().slideToggle('fast');
		$('.accordion-content').not($(this).next()).slideUp('fast');
		$('.accordion-title').not($(this)).removeClass('active');		
	});
	
	/*====================
	WOW JS
	======================*/
	new WOW().init();
		
	/*====================
	POPUP JS
	======================*/
	$('.popup-youtube, .popup-vimeo').magnificPopup({
		disableOn: 300,
		type: 'iframe',
		mainClass: 'mfp-fade',
		removalDelay: 160,
		preloader: false,
		fixedContentPos: false,
	});

	/*====================
	Tabs JS
	======================*/
	$('.tab ul.tabs').addClass('active').find('> li:eq(0)').addClass('current');
	$('.tab ul.tabs li').on('click', function (g) {
		var tab = $(this).closest('.tab'), 
		index = $(this).closest('li').index();
		tab.find('ul.tabs > li').removeClass('current');
		$(this).closest('li').addClass('current');
		tab.find('.tab_content').find('div.tabs_item').not('div.tabs_item:eq(' + index + ')').fadeOut();
		tab.find('.tab_content').find('div.tabs_item:eq(' + index + ')').fadeIn();
		g.preventDefault();
	});

	/*====================
	INPUT COUNTER JS
	======================*/
	$('.input-counter').each(function() {
		var spinner = jQuery(this),
		input = spinner.find('input[type="text"]'),
		btnUp = spinner.find('.plus-btn'),
		btnDown = spinner.find('.minus-btn'),
		min = input.attr('min'),
		max = input.attr('max');
		
		btnUp.on('click', function() {
			var oldValue = parseFloat(input.val());
			if (oldValue >= max) {
				var newVal = oldValue;
			} else {
				var newVal = oldValue + 1;
			}
			spinner.find("input").val(newVal);
			spinner.find("input").trigger("change");
		});
		btnDown.on('click', function() {
			var oldValue = parseFloat(input.val());
			if (oldValue <= min) {
				var newVal = oldValue;
			} else {
				var newVal = oldValue - 1;
			}
			spinner.find("input").val(newVal);
			spinner.find("input").trigger("change");
		});
	});

	
	/*====================
	SUBSCRIBE FORM JS
	======================*/
	$(".newsletter-form").validator().on("submit", function (event) {
		if (event.isDefaultPrevented()) {
		// handle the invalid form...
			formErrorSub();
			submitMSGSub(false, "Please enter your email correctly.");
		} else {
			// everything looks good!
			event.preventDefault();
		}
	});
	function callbackFunction (resp) {
		if (resp.result === "success") {
			formSuccessSub();
		}
		else {
			formErrorSub();
		}
	}
	function formSuccessSub(){
		$(".newsletter-form")[0].reset();
		submitMSGSub(true, "Thank you for subscribing!");
		setTimeout(function() {
			$("#validator-newsletter").addClass('hide');
		}, 4000)
	}
	function formErrorSub(){
		$(".newsletter-form").addClass("animated shake");
		setTimeout(function() {
			$(".newsletter-form").removeClass("animated shake");
		}, 1000)
	}
	function submitMSGSub(valid, msg){
		if(valid){
			var msgClasses = "validation-success";
		} else {
			var msgClasses = "validation-danger";
		}
		$("#validator-newsletter").removeClass().addClass(msgClasses).text(msg);
	}
	// AJAX MailChimp
	$(".newsletter-form").ajaxChimp({
		url: "https://envytheme.us20.list-manage.com/subscribe/post?u=60e1ffe2e8a68ce1204cd39a5&amp;id=42d6d188d9", // Your url MailChimp
		callback: callbackFunction
	});
	
	// Stop Right Click
    /*$(document).on({
        "contextmenu": function(e) {
            console.log("ctx menu button:", e.which);

            // Stop the context menu
            e.preventDefault();
        },
        "mousedown": function(e) {
            console.log("normal mouse down:", e.which);
        },
        "mouseup": function(e) {
            console.log("normal mouse up:", e.which);
        }
    });*/
	
})(jQuery);
