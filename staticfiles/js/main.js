$(document).on("click", ".member-1", function () { $(".detail-box-1").toggleClass("show-details-1"), $(".detail-box-2").removeClass("show-details-2"), $(".detail-box-3").removeClass("show-details-3"), $(".detail-box-4").removeClass("show-details-4"), $(".detail-box-5").removeClass("show-details-5"), $(".detail-box-6").removeClass("show-details-6") }), $(document).on("click", ".member-2", function () { $(".detail-box-2").toggleClass("show-details-2"), $(".detail-box-1").removeClass("show-details-1"), $(".detail-box-3").removeClass("show-details-3"), $(".detail-box-4").removeClass("show-details-4"), $(".detail-box-5").removeClass("show-details-5"), $(".detail-box-6").removeClass("show-details-6") }), $(document).on("click", ".member-3", function () { $(".detail-box-3").toggleClass("show-details-3"), $(".detail-box-2").removeClass("show-details-2"), $(".detail-box-1").removeClass("show-details-1"), $(".detail-box-4").removeClass("show-details-4"), $(".detail-box-5").removeClass("show-details-5"), $(".detail-box-6").removeClass("show-details-6") }), $(document).on("click", ".member-4", function () { $(".detail-box-4").toggleClass("show-details-4"), $(".detail-box-2").removeClass("show-details-2"), $(".detail-box-3").removeClass("show-details-3"), $(".detail-box-1").removeClass("show-details-1"), $(".detail-box-5").removeClass("show-details-5"), $(".detail-box-6").removeClass("show-details-6") }), $(document).on("click", ".member-5", function () { $(".detail-box-5").toggleClass("show-details-5"), $(".detail-box-2").removeClass("show-details-2"), $(".detail-box-3").removeClass("show-details-3"), $(".detail-box-4").removeClass("show-details-4"), $(".detail-box-1").removeClass("show-details-1"), $(".detail-box-6").removeClass("show-details-6") }), $(document).on("click", ".member-6", function () { $(".detail-box-6").toggleClass("show-details-6"), $(".detail-box-2").removeClass("show-details-2"), $(".detail-box-3").removeClass("show-details-3"), $(".detail-box-4").removeClass("show-details-4"), $(".detail-box-5").removeClass("show-details-5"), $(".detail-box-1").removeClass("show-details-1") }), $(document).on("click", ".cancel", function () { $(".detail-box-1").removeClass("show-details-1"), $(".detail-box-2").removeClass("show-details-2"), $(".detail-box-3").removeClass("show-details-3"), $(".detail-box-4").removeClass("show-details-4"), $(".detail-box-5").removeClass("show-details-5"), $(".detail-box-6").removeClass("show-details-6"), $(".detail-box-7").removeClass("show-details-7"), $(".detail-box-8").removeClass("show-details-8") }), $(document).ready(function () { $(".back-to-top").click(function () { $("html ,body").animate({ scrollTop: 0 }, 1500) }), $('[data-toggle="counter-up"]').counterUp({ delay: 10, time: 2500 }); new SimpleLightbox(".featured-project a", {}), new SimpleLightbox(".pro-details a", {}), new SimpleLightbox(".gallery a", {}); (new WOW).init(), $(".carousel").carousel({ interval: 15e3 }), $("#services").owlCarousel({ loop: !0, margin: 10, nav: !1, width: 1200, animateOut: "fadeOut", animateIn: "fadeIn", items: 1, responsive: { 320: { items: 1 }, 375: { items: 1 }, 480: { items: 1 }, 576: { items: 2 }, 768: { items: 2 }, 992: { items: 3 }, 1200: { items: 3 } } }), $("#pricing").owlCarousel({ loop: !0, margin: 10, nav: !1, width: 1280, animateOut: "fadeOut", animateIn: "fadeIn", items: 1, responsive: { 320: { items: 1 }, 375: { items: 1 }, 480: { items: 1 }, 576: { items: 2 }, 768: { items: 2 }, 992: { items: 3 }, 1200: { items: 4 } } }), $("#vision").owlCarousel({ loop: !0, margin: 10, nav: !1, width: 1200, animateOut: "fadeOut", animateIn: "fadeIn", items: 1, responsive: { 320: { items: 1 }, 375: { items: 1 }, 480: { items: 1 }, 576: { items: 2 }, 768: { items: 2 }, 992: { items: 3 } } }), $("#core").owlCarousel({ loop: !0, margin: 10, nav: !1, width: 1200, animateOut: "fadeOut", animateIn: "fadeIn", items: 1, responsive: { 320: { items: 1 }, 375: { items: 1 }, 480: { items: 1 }, 576: { items: 2 }, 768: { items: 2 }, 992: { items: 3 }, 1200: { items: 4 } } }), $("#team-one").owlCarousel({ loop: !0, margin: 10, nav: !1, width: 1200, animateOut: "fadeOut", animateIn: "fadeIn", items: 1, responsive: { 320: { items: 1 }, 375: { items: 1 }, 480: { items: 1 }, 576: { items: 2 }, 768: { items: 2 }, 992: { items: 3 } } }), $("#testimonial").owlCarousel({ loop: !0, margin: 0, nav: !1, dots: !0, autoWidth: !1, autoplay: !0, smartSpeed: 1e3, autoplayTimeout: 9e3, autoplayHoverPause: !0, responsive: { 320: { items: 1 }, 767: { items: 1 }, 960: { items: 1 } } }), $("#project").owlCarousel({ loop: !0, margin: 10, nav: !1, dots: !0, autoplay: !0, smartSpeed: 700, width: 1200, animateOut: "fadeOut", animateIn: "fadeIn", items: 1, responsive: { 320: { items: 1 }, 375: { items: 1 }, 480: { items: 1 }, 576: { items: 2 }, 768: { items: 2 }, 991: { items: 3 }, 1200: { items: 4 } } }), $("#featured-project").owlCarousel({ loop: !0, margin: 10, nav: !1, width: 1200, autoplay: !0, smartSpeed: 700, autoplayTimeout: 5e3, autoplayHoverPause: !0, animateOut: "fadeOut", animateIn: "fadeIn", items: 1, responsive: { 320: { items: 1 }, 375: { items: 1 }, 480: { items: 1 }, 576: { items: 2 }, 768: { items: 2 }, 992: { items: 3 }, 1200: { items: 4 } } }), $(".brand-carousel-one").owlCarousel({ loop: !0, margin: 10, nav: !1, navText: ['<i class="fa fa-long-arrow-left"></i>', '<i class="fa fa-long-arrow-right"></i>'], dots: !0, autoWidth: !1, autoplay: !0, smartSpeed: 700, autoplayTimeout: 5e3, autoplayHoverPause: !0, responsive: { 320: { items: 1 }, 480: { items: 2 }, 600: { items: 3 }, 991: { items: 4 }, 1e3: { items: 5 }, 1200: { items: 5 } } }), $(document).ready(function () { $(window).scroll(function () { 80 < $(this).scrollTop() ? $(".back-to-top").fadeIn() : $(".back-to-top").fadeOut() }) }), $(".collapse").collapse() }), $(function () { $(".js-sticky-header").sticky({ topSpacing: 0 }); $(".js-clone-nav").each(function () { $(this).clone().attr("class", "site-nav-wrap").appendTo(".site-mobile-menu-body") }), setTimeout(function () { var s = 0; $(".site-mobile-menu .has-children").each(function () { var e = $(this); e.prepend('<span class="arrow-collapse collapsed">'), e.find(".arrow-collapse").attr({ "data-toggle": "collapse", "data-target": "#collapseItem" + s }), e.find("> ul").attr({ class: "collapse", id: "collapseItem" + s }), s++ }) }, 1e3), $("body").on("click", ".arrow-collapse", function (e) { var s = $(this); s.closest("li").find(".collapse").hasClass("show") ? s.removeClass("active") : s.addClass("active"), e.preventDefault() }), $(window).resize(function () { 768 < $(this).width() && $("body").hasClass("offcanvas-menu") && $("body").removeClass("offcanvas-menu") }), $("body").on("click", ".js-menu-toggle", function (e) { var s = $(this); e.preventDefault(), $("body").hasClass("offcanvas-menu") ? ($("body").removeClass("offcanvas-menu"), s.removeClass("active")) : ($("body").addClass("offcanvas-menu"), s.addClass("active")) }), $(document).mouseup(function (e) { var s = $(".site-mobile-menu"); s.is(e.target) || 0 !== s.has(e.target).length || $("body").hasClass("offcanvas-menu") && $("body").removeClass("offcanvas-menu") }) });