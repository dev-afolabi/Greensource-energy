    $(document).on('click','.member-1',function(){
    $('.detail-box-1').toggleClass('show-details-1')
    $('.detail-box-2').removeClass('show-details-2')
    $('.detail-box-3').removeClass('show-details-3')
    $('.detail-box-4').removeClass('show-details-4')
    $('.detail-box-5').removeClass('show-details-5')
    $('.detail-box-6').removeClass('show-details-6')
});
$(document).on('click','.member-2',function(){
    $('.detail-box-2').toggleClass('show-details-2')
    $('.detail-box-1').removeClass('show-details-1')
    $('.detail-box-3').removeClass('show-details-3')
    $('.detail-box-4').removeClass('show-details-4')
    $('.detail-box-5').removeClass('show-details-5')
    $('.detail-box-6').removeClass('show-details-6')
});
$(document).on('click','.member-3',function(){
    $('.detail-box-3').toggleClass('show-details-3')
    $('.detail-box-2').removeClass('show-details-2')
    $('.detail-box-1').removeClass('show-details-1')
    $('.detail-box-4').removeClass('show-details-4')
    $('.detail-box-5').removeClass('show-details-5')
    $('.detail-box-6').removeClass('show-details-6')
});
$(document).on('click','.member-4',function(){
    $('.detail-box-4').toggleClass('show-details-4')
    $('.detail-box-2').removeClass('show-details-2')
    $('.detail-box-3').removeClass('show-details-3')
    $('.detail-box-1').removeClass('show-details-1')
    $('.detail-box-5').removeClass('show-details-5')
    $('.detail-box-6').removeClass('show-details-6')
});
$(document).on('click','.member-5',function(){
    $('.detail-box-5').toggleClass('show-details-5')
    $('.detail-box-2').removeClass('show-details-2')
    $('.detail-box-3').removeClass('show-details-3')
    $('.detail-box-4').removeClass('show-details-4')
    $('.detail-box-1').removeClass('show-details-1')
    $('.detail-box-6').removeClass('show-details-6')
});
$(document).on('click','.member-6',function(){
    $('.detail-box-6').toggleClass('show-details-6')
    $('.detail-box-2').removeClass('show-details-2')
    $('.detail-box-3').removeClass('show-details-3')
    $('.detail-box-4').removeClass('show-details-4')
    $('.detail-box-5').removeClass('show-details-5')
    $('.detail-box-1').removeClass('show-details-1')
});
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
    $('.back-to-top').click(function () {
        $('html ,body').animate({ scrollTop: 0 }, 1500);
    });
    
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2500
    });

    var lightbox = new SimpleLightbox('.featured-project a', {});
   
    var lightbox = new SimpleLightbox('.pro-details a', {});

    var lightbox = new SimpleLightbox('.gallery a', {});
    new WOW().init();

    $('.carousel').carousel({
        interval: 15000,
    });
    
    $('#services').owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        width: 1200,
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',
        items: 1,
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
    $('#pricing').owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        width: 1280,
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',
        items: 1,
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
                items: 4
            }
        }
    });
    $('#vision').owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        width: 1200,
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',
        items: 1,
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
            }
        }
    });
    $('#core').owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        width: 1200,
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',
        items: 1,
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
                items: 4
            }
        }
    });
    $('#team-one').owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        width: 1200,
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',
        items: 1,
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
            }
        }
    });
    $('#testimonial').owlCarousel({
        loop: true,
        margin: 0,
        nav: false,
        dots: true,
        autoWidth: false,
        autoplay: true,
        smartSpeed: 1000,
        autoplayTimeout: 9000,
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
    $('#project').owlCarousel({
            loop: true,
            margin: 10,
            nav: false,
            dots: true,
            autoplay: true,
            smartSpeed: 700,
            width: 1200,
            animateOut: 'fadeOut',
            animateIn: 'fadeIn',
            items: 1,
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
                991: {
                    items: 3
                },
                1200: {
                    items: 4
                }
            }
    });
    $('#featured-project').owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        width: 1200,
        autoplay: true,
        smartSpeed: 700,
        autoplayTimeout: 5000,
        autoplayHoverPause: true,
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',
        items: 1,
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
                items: 4
            }
        }
    });
    $('#landing-page').owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        dots: true,
        autoplay: true,
        smartSpeed: 700,
        width: 1200,
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',
        items: 1,
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
            991: {
                items: 3
            },
            1200: {
                items: 4
            }
        }
    });
    $(document).ready(function () {
        $(window).scroll(function () {
            if ($(this).scrollTop() > 80) {
                $('.back-to-top').fadeIn();
            } else {
                $('.back-to-top').fadeOut();
            }
        });
    });
    $('.collapse').collapse();

});
$(function() {

    var siteSticky = function() {
          $(".js-sticky-header").sticky({topSpacing:0});
      };
      siteSticky();
  
      var siteMenuClone = function() {
  
          $('.js-clone-nav').each(function() {
              var $this = $(this);
              $this.clone().attr('class', 'site-nav-wrap').appendTo('.site-mobile-menu-body');
          });
  
  
          setTimeout(function() {
              
              var counter = 0;
        $('.site-mobile-menu .has-children').each(function(){
          var $this = $(this);
          
          $this.prepend('<span class="arrow-collapse collapsed">');
  
          $this.find('.arrow-collapse').attr({
            'data-toggle' : 'collapse',
            'data-target' : '#collapseItem' + counter,
          });
  
          $this.find('> ul').attr({
            'class' : 'collapse',
            'id' : 'collapseItem' + counter,
          });
  
          counter++;
  
        });
  
      }, 1000);
  
          $('body').on('click', '.arrow-collapse', function(e) {
        var $this = $(this);
        if ( $this.closest('li').find('.collapse').hasClass('show') ) {
          $this.removeClass('active');
        } else {
          $this.addClass('active');
        }
        e.preventDefault();  
        
      });
  
          $(window).resize(function() {
              var $this = $(this),
                  w = $this.width();
  
              if ( w > 768 ) {
                  if ( $('body').hasClass('offcanvas-menu') ) {
                      $('body').removeClass('offcanvas-menu');
                  }
              }
          })
  
          $('body').on('click', '.js-menu-toggle', function(e) {
              var $this = $(this);
              e.preventDefault();
  
              if ( $('body').hasClass('offcanvas-menu') ) {
                  $('body').removeClass('offcanvas-menu');
                  $this.removeClass('active');
              } else {
                  $('body').addClass('offcanvas-menu');
                  $this.addClass('active');
              }
          }) 
  
          $(document).mouseup(function(e) {
          var container = $(".site-mobile-menu");
          if (!container.is(e.target) && container.has(e.target).length === 0) {
            if ( $('body').hasClass('offcanvas-menu') ) {
                      $('body').removeClass('offcanvas-menu');
                  }
          }
          });
      }; 
      siteMenuClone();
});
$(function() {
    (function (w, d, s, l, i) {
    w[l] = w[l] || []; w[l].push({
        'gtm.start':
            new Date().getTime(), event: 'gtm.js'
    }); var f = d.getElementsByTagName(s)[0],
        j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : ''; j.async = true; j.src =
            'https://www.googletagmanager.com/gtm.js?id=' + i + dl; f.parentNode.insertBefore(j, f);
    })(window, document, 'script', 'dataLayer', 'GTM-W2SS447');
});
$(function() {
var url = 'https://wati-integration-service.clare.ai/ShopifyWidget/shopifyWidget.js?28293';
var s = document.createElement('script');
s.type = 'text/javascript';
s.async = true;
s.src = url;
var options = {
    "enabled": true,
    "chatButtonSetting": {
        "backgroundColor": "#28D146",
        "ctaText": "",
        "borderRadius": "45",
        "marginLeft": "0",
        "marginBottom": "10",
        "marginRight": "10",
        "position": "right"
    },
    "brandSetting": {
        "brandName": "OLUJOSEPH",
        "brandSubTitle": "Solar PV Designer",
        "brandImg": "https://greensourcenergy.com/static/images/ceo.webp",
        "welcomeText": "Hi there!\nNeed a custom solar solution for your Home or Business? We would design one for you !\n",
        "messageText": "{{page_title}}Hello, I have a question about {{page_link}}{{page_link}}",
        "backgroundColor": "#007654",
        "ctaText": "Chat me Up",
        "borderRadius": "45",
        "autoShow": false,
        "phoneNumber": "2349132909546"
    }
};
s.onload = function () {
    CreateWhatsappChatWidget(options);
};
var x = document.getElementsByTagName('script')[0];
x.parentNode.insertBefore(s, x);
});


