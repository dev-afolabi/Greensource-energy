 /*-1-----------------------------------*/
 $(document).on('click','.member-1',function(){
    $('.detail-box-1').toggleClass('show-details-1')
    $('.detail-box-2').removeClass('show-details-2')
    $('.detail-box-3').removeClass('show-details-3')
    $('.detail-box-4').removeClass('show-details-4')
    $('.detail-box-5').removeClass('show-details-5')
    $('.detail-box-6').removeClass('show-details-6')
});
/*-2-----------------------------------*/
$(document).on('click','.member-2',function(){
    $('.detail-box-2').toggleClass('show-details-2')
    $('.detail-box-1').removeClass('show-details-1')
    $('.detail-box-3').removeClass('show-details-3')
    $('.detail-box-4').removeClass('show-details-4')
    $('.detail-box-5').removeClass('show-details-5')
    $('.detail-box-6').removeClass('show-details-6')
});
/*-3-----------------------------------*/
$(document).on('click','.member-3',function(){
    $('.detail-box-3').toggleClass('show-details-3')
    $('.detail-box-2').removeClass('show-details-2')
    $('.detail-box-1').removeClass('show-details-1')
    $('.detail-box-4').removeClass('show-details-4')
    $('.detail-box-5').removeClass('show-details-5')
    $('.detail-box-6').removeClass('show-details-6')
});
/*-4-----------------------------------*/
$(document).on('click','.member-4',function(){
    $('.detail-box-4').toggleClass('show-details-4')
    $('.detail-box-2').removeClass('show-details-2')
    $('.detail-box-3').removeClass('show-details-3')
    $('.detail-box-1').removeClass('show-details-1')
    $('.detail-box-5').removeClass('show-details-5')
    $('.detail-box-6').removeClass('show-details-6')
});
/*-5-----------------------------------*/
$(document).on('click','.member-5',function(){
    $('.detail-box-5').toggleClass('show-details-5')
    $('.detail-box-2').removeClass('show-details-2')
    $('.detail-box-3').removeClass('show-details-3')
    $('.detail-box-4').removeClass('show-details-4')
    $('.detail-box-1').removeClass('show-details-1')
    $('.detail-box-6').removeClass('show-details-6')
});
/*-6-----------------------------------*/
$(document).on('click','.member-6',function(){
    $('.detail-box-6').toggleClass('show-details-6')
    $('.detail-box-2').removeClass('show-details-2')
    $('.detail-box-3').removeClass('show-details-3')
    $('.detail-box-4').removeClass('show-details-4')
    $('.detail-box-5').removeClass('show-details-5')
    $('.detail-box-1').removeClass('show-details-1')
});

/*-cancel------------------*/
$(document).on('click','.cancel',function(){
    $('.detail-box-1').removeClass('show-details-1')
    $('.detail-box-2').removeClass('show-details-2')
    $('.detail-box-3').removeClass('show-details-3')
    $('.detail-box-4').removeClass('show-details-4')
    $('.detail-box-5').removeClass('show-details-5')
    $('.detail-box-6').removeClass('show-details-6')
    $('.detail-box-7').removeClass('show-details-7')
    $('.detail-box-8').removeClass('show-details-8') 
});

$(document).ready(function () {
    if ($('#nav-menu-container').length) {
        var $mobile_nav = $('#nav-menu-container').clone().prop({ id: 'mobile-nav' });
        $mobile_nav.find('> ul').attr({ 'class': '', 'id': '' });
        $('body').append($mobile_nav);
        $('body').prepend('<button type="button" id="mobile-nav-toggle"><i class="fa fa-bars"></i></button>');
        $('body').append('<div id="mobile-body-overly"></div>');
        $('#mobile-nav').find('.menu-has-children').prepend('<i class="fa fa-chevron-down"></i>');
        $(document).on('click', '.menu-has-children i', function (e) {
            $(this).next().toggleClass('menu-item-active');
            $(this).nextAll('ul').eq(0).slideToggle();
            $(this).toggleClass("fa-chevron-up fa-chevron-down");
        });
        $(document).on('click', '#mobile-nav-toggle', function (e) {
            $('body').toggleClass('mobile-nav-active');
            $('#mobile-nav-toggle i').toggleClass('fa-times fa-bars');
            $('#mobile-body-overly').toggle();
        });
        $(document).click(function (e) {
            var container = $("#mobile-nav, #mobile-nav-toggle");
            if (!container.is(e.target) && container.has(e.target).length === 0) {
                if ($('body').hasClass('mobile-nav-active')) {
                    $('body').removeClass('mobile-nav-active');
                    $('#mobile-nav-toggle i').toggleClass('fa-times fa-bars');
                    $('#mobile-body-overly').fadeOut();
                }
            }
        });
    } else if ($("#mobile-nav, #mobile-nav-toggle").length) {
        $("#mobile-nav, #mobile-nav-toggle").hide();
    }
    $('.nav-menu').superfish({
        animation: { opacity: 'show' },
        speed: 400
    });
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2500
    });
   
    var lightbox = new SimpleLightbox('.gallery a', {});
    new WOW().init();
    $('.carousel').carousel({
        interval: 15000,
    });
    $('#bridgeSlide').owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        width: 1200,
        autoplay: false,
        smartSpeed: 700,
        responsive: {
            320: {
                items: 1
            },
            375: {
                items: 1
            },
            480: {
                items: 1
            },
            577: {
                items: 2
            },
            767: {
                items: 2
            },
            992: {
                items: 3
            },
            1200: {
                items: 3
            }
        }
    });
    $('#pricing').owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        width: 1200,
        autoplay: true,
        smartSpeed: 700,
        responsive: {
            320: {
                items: 1
            },
            375: {
                items: 1
            },
            480: {
                items: 1
            },
            577: {
                items: 1
            },
            767: {
                items: 3
            },
            992: {
                items: 4
            },
            1200: {
                items: 4
            }
        }
    });
    $('#mission').owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        width: 1200,
        responsive: {
            320: {
                items: 1
            },
            375: {
                items: 1
            },
            480: {
                items: 1
            },
            576: {
                items: 1
            },
            768: {
                items: 2
            },
            992: {
                items: 3
            }
        }
    });
    $('#team-one').owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        width: 1200,
        responsive: {
            320: {
                items: 1
            },
            375: {
                items: 1
            },
            480: {
                items: 1
            },
            576: {
                items: 2
            },
            768: {
                items: 2
            },
            992: {
                items: 3
            },
            1200: {
                items: 3
            }
        }
    });
    $('#test').owlCarousel({
        loop: true,
        margin: 0,
        nav: false,
        dots: true,
        autoWidth: false,
        autoplay: true,
        smartSpeed: 700,
        autoplayTimeout: 5000,
        autoplayHoverPause: true,
        responsive: {
            320: {
                items: 1
            },
            767: {
                items: 1
            },
            960: {
                items: 1
            }
        }
    });
    if ($('.brand-carousel-one').length) {
        $('.brand-carousel-one').owlCarousel({
            loop: true,
            margin: 10,
            nav: false,
            navText: [
                '<i class="fa fa-long-arrow-left"></i>',
                '<i class="fa fa-long-arrow-right"></i>'
            ],
            dots: false,
            autoWidth: false,
            autoplay: true,
            smartSpeed: 700,
            autoplayTimeout: 5000,
            autoplayHoverPause: true,
            responsive: {
                0: {
                    items: 1
                },
                480: {
                    items: 3
                },
                600: {
                    items: 3
                },
                991: {
                    items: 4
                },
                1000: {
                    items: 5
                },
                1200: {
                    items: 5
                }
            }
        });
    }
    $(document).ready(function () {
        $(window).scroll(function () {
            if ($(this).scrollTop() > 80) {
                $('.back-to-top').fadeIn();
            } else {
                $('.back-to-top').fadeOut();
            }
        });
    });
    $('.back-to-top').click(function () {
        $('html ,body').animate({ scrollTop: 0 }, 1500);
    });
    $('.collapse').collapse();
});
$(document).ready(function () {
    ToxProgress.create();
    ToxProgress.animate();
});
window.addEventListener("scroll", function(){
    var header = document.querySelector("header");
    header.classList.toggle("header-fixed", window.scrollY > 0);
});

function incrementValue(){
    var value = parseInt(document.getElementById('text').value, 10);
    value = isNaN(value) ? 0 : value;
    if(value<10){
        value++;
            document.getElementById('text').value = value; 
    }
}
function decrementValue(){
    var value = parseInt(document.getElementById('text').value, 10);
    value = isNaN(value) ? 0 : value;
    if(value>1){
        value--;
            document.getElementById('text').value = value; 
    }
}

const count = new Date('jun 1,2021 00:00:00').getTime()
var x = setInterval(() => {
  const now = new Date().getTime()
  const d = count - now

  const days = Math.floor(d / (1000 * 60 * 60 * 24))
  const hours = Math.floor((d % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
  const minutes = Math.floor((d % (1000 * 60 * 60)) / (1000 * 60))
  const seconds = Math.floor((d % (1000 * 60)) / 1000)

  document.getElementById('days').innerHTML = days
  document.getElementById('hours').innerHTML = hours
  document.getElementById('minutes').innerHTML = minutes
  document.getElementById('seconds').innerHTML = seconds

  if (d <= 0) {
    clearInterval(x)
  }
}, 1000)

window.cookieconsent.initialise({
    "palette": {
        "popup": {
            "background": "#3c404d",
            "text": "#d6d6d6"
        },
        "button": {
            "background": "transparent",
            "text": "#89af3b",
            "border": "#89af3b"
        }
    },
    "content": {
        "href": "{% url 'privacy' %}"
    },

    "position": "bottom-left"
});

