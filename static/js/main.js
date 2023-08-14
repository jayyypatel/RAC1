(function($) {
    "use strict";

    function backgroundImage() {
        var databackground = $('[data-background]');
        databackground.each(function() {
            if ($(this).attr('data-background')) {
                var image_path = $(this).attr('data-background');
                $(this).css({
                    'background': 'url(' + image_path + ')'
                });
            }
        });
    }

    function siteToggleAction() {
        var navSidebar = $('.navigation--sidebar'),
            filterSidebar = $('.ps-filter--sidebar');
        $('.menu-toggle-open').on('click', function(e) {
            e.preventDefault();
            $(this).toggleClass('active')
            navSidebar.toggleClass('active');
            $('.ps-site-overlay').toggleClass('active');
        });

        $('.ps-toggle--sidebar').on('click', function(e) {
            e.preventDefault();
            var url = $(this).attr('href');
            $(this).toggleClass('active');
            $(this).siblings('a').removeClass('active');
            $(url).toggleClass('active');
            $(url).siblings('.ps-panel--sidebar').removeClass('active');
            $('.ps-site-overlay').toggleClass('active');
        });

        $('#filter-sidebar').on('click', function(e) {
            e.preventDefault();
            filterSidebar.addClass('active');
            $('.ps-site-overlay').addClass('active');
        });

        $('.ps-filter--sidebar .ps-filter__header .ps-btn--close').on('click', function(e) {
            e.preventDefault();
            filterSidebar.removeClass('active');
            $('.ps-site-overlay').removeClass('active');
        });

        $('body').on("click", function(e) {
            if ($(e.target).siblings(".ps-panel--sidebar").hasClass('active')) {
                $('.ps-panel--sidebar').removeClass('active');
                $('.ps-site-overlay').removeClass('active');
            }
        });
    }

    function subMenuToggle() {
        $('.menu--mobile .menu-item-has-children > .sub-toggle').on('click', function(e) {
            e.preventDefault();
            var current = $(this).parent('.menu-item-has-children')
            $(this).toggleClass('active');
            current.siblings().find('.sub-toggle').removeClass('active');
            current.children('.sub-menu').slideToggle(350);
            current.siblings().find('.sub-menu').slideUp(350);

        });
    }

    function stickyHeader() {
        var header = $('.header'),
            checkpoint = 50;
        if (header.data('sticky') === true) {
            $(window).scroll(function() {
                var currentPosition = $(this).scrollTop();
                if (currentPosition > checkpoint) {
                    header.addClass('header--sticky');
                } else {
                    header.removeClass('header--sticky');
                }
            });
        } else {
            return false;
        }
    }

    function owlCarouselConfig() {
        var target = $('.owl-slider');
        if (target.length > 0) {
            target.each(function() {
                var el = $(this),
                    dataAuto = el.data('owl-auto'),
                    dataLoop = el.data('owl-loop'),
                    dataSpeed = el.data('owl-speed'),
                    dataGap = el.data('owl-gap'),
                    dataNav = el.data('owl-nav'),
                    dataDots = el.data('owl-dots'),
                    dataAnimateIn = (el.data('owl-animate-in')) ? el.data('owl-animate-in') : '',
                    dataAnimateOut = (el.data('owl-animate-out')) ? el.data('owl-animate-out') : '',
                    dataDefaultItem = el.data('owl-item'),
                    dataItemXS = el.data('owl-item-xs'),
                    dataItemSM = el.data('owl-item-sm'),
                    dataItemMD = el.data('owl-item-md'),
                    dataItemLG = el.data('owl-item-lg'),
                    dataItemXL = el.data('owl-item-xl'),
                    dataNavLeft = (el.data('owl-nav-left')) ? el.data('owl-nav-left') : "<i class='fa fa-angle-left'></i>",
                    dataNavRight = (el.data('owl-nav-right')) ? el.data('owl-nav-right') : "<i class='fa fa-angle-right'></i>",
                    duration = el.data('owl-duration'),
                    datamouseDrag = (el.data('owl-mousedrag') == 'on') ? true : false;
                if (target.children('div, span, a, img, h1, h2, h3, h4, h5, h5').length >= 2) {
                    el.owlCarousel({
                        animateIn: dataAnimateIn,
                        animateOut: dataAnimateOut,
                        margin: dataGap,
                        autoplay: dataAuto,
                        autoplayTimeout: dataSpeed,
                        autoplayHoverPause: true,
                        loop: dataLoop,
                        nav: dataNav,
                        mouseDrag: datamouseDrag,
                        touchDrag: true,
                        autoplaySpeed: duration,
                        navSpeed: duration,
                        dotsSpeed: duration,
                        dragEndSpeed: duration,
                        navText: [dataNavLeft, dataNavRight],
                        dots: dataDots,
                        items: dataDefaultItem,
                        responsive: {
                            0: {
                                items: dataItemXS
                            },
                            480: {
                                items: dataItemSM
                            },
                            768: {
                                items: dataItemMD
                            },
                            992: {
                                items: dataItemLG
                            },
                            1200: {
                                items: dataItemXL
                            },
                            1680: {
                                items: dataDefaultItem
                            }
                        }
                    });
                }
            });
        }
        var owlNavigate = $(".ps-carousel-nav li a");
        owlNavigate.on('click', function(e) {
            e.preventDefault();
            var slider = $(this).closest('ul').data('target');
            $(slider).owlCarousel();
            $(slider).trigger('to.owl.carousel', $(this).data('index'), [300], true);
        });
    }

    function masonry($selector) {
        var masonry = $($selector);
        if (masonry.length > 0) {
            if (masonry.hasClass('filter')) {
                masonry.imagesLoaded(function() {
                    masonry.isotope({
                        columnWidth: '.grid-sizer',
                        itemSelector: '.grid-item',
                        isotope: {
                            columnWidth: '.grid-sizer'
                        },
                        filter: "*"
                    });
                });
                var filters = masonry.closest('.masonry-root').find('.ps-masonry-filter > li > a');
                filters.on('click', function(e) {
                    e.preventDefault();
                    var selector = $(this).attr('href');
                    filters.find('a').removeClass('current');
                    $(this).parent('li').addClass('current');
                    $(this).parent('li').siblings('li').removeClass('current');
                    $(this).closest('.masonry-root').find('.ps-masonry').isotope({
                        itemSelector: '.grid-item',
                        isotope: {
                            columnWidth: '.grid-sizer'
                        },
                        filter: selector
                    });
                    return false;
                });
            } else {
                masonry.imagesLoaded(function() {
                    masonry.masonry({
                        columnWidth: '.grid-sizer',
                        itemSelector: '.grid-item'
                    });
                });
            }
        }
    }

    function tabs() {
        $('.ps-tab-list  li > a ').on('click', function(e) {
            e.preventDefault();
            var target = $(this).attr('href');
            $(this).closest('li').siblings('li').removeClass('active');
            $(this).closest('li').addClass('active');
            $(target).addClass('active');
            $(target).siblings('.ps-tab').removeClass('active');
        });
        $('.ps-tab-list.owl-slider .owl-item a').on('click', function(e) {
            e.preventDefault();
            var target = $(this).attr('href');
            $(this).closest('.owl-item').siblings('.owl-item').removeClass('active');
            $(this).closest('.owl-item').addClass('active');
            $(target).addClass('active');
            $(target).siblings('.ps-tab').removeClass('active');
        });
    }

    function rating() {
        $('select.ps-rating').each(function() {
            var readOnly;
            if ($(this).attr('data-read-only') == 'true') {
                readOnly = true
            } else {
                readOnly = false;
            }
            $(this).barrating({
                theme: 'fontawesome-stars',
                readonly: readOnly,
                emptyValue: '0'
            });
        });
    }

    function modalInit() {
        var modal = $('.ps-modal');
        if (modal.length) {
            if (modal.hasClass('active')) {
                $('body').css('overflow-y', 'hidden');
            }
        }

        modal.find('.ps-modal__close, .ps-btn--close').on('click', function(e) {
            e.preventDefault();
            $(this).closest('.ps-modal').removeClass('active');
            $("body").css('overflow-y', 'auto');
        });

        $('.ps-modal-link').on('click', function(e) {
            e.preventDefault();
            var target = $(this).attr('href');
            $(target).addClass('active');
            $("body").css('overflow-y', 'hidden');
        });

        $('.ps-modal').on("click", function(event) {
            if (!$(event.target).closest(".ps-modal__container").length) {
                modal.removeClass('active');
                $("body").css('overflow-y', 'auto');
            }
        });
    }

    function searchInit() {
        var searchbox = $('.ps-search');
        $('.ps-search-btn').on('click', function(e) {
            e.preventDefault();
            searchbox.addClass('active');
        });
        searchbox.find('.ps-btn--close').on('click', function(e) {
            e.preventDefault();
            searchbox.removeClass('active');
        });
    }

    function countDown() {
        var time = $(".ps-countdown");
        time.each(function() {
            var el = $(this),
                value = $(this).data('time');
            var countDownDate = new Date(value).getTime();
            var timeout = setInterval(function() {
                var now = new Date().getTime(),
                    distance = countDownDate - now;
                var days = Math.floor(distance / (1000 * 60 * 60 * 24)),
                    hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)),
                    minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60)),
                    seconds = Math.floor((distance % (1000 * 60)) / 1000);
                el.find('.days').html(days);
                el.find('.hours').html(hours);
                el.find('.minutes').html(minutes);
                el.find('.seconds').html(seconds);
                if (distance < 0) {
                    clearInterval(timeout);
                    el.closest('.ps-section').hide();
                }
            }, 1000);
        });
    }

    function subscribePopup() {
        var subscribe = $('#subscribe'),
            time = subscribe.data('time');
        setTimeout(function() {
            if (subscribe.length > 0) {
                subscribe.addClass('active');
                $('body').css('overflow', 'hidden');
            }
        }, time);
        $('.ps-popup__close').on('click', function(e) {
            e.preventDefault();
            $(this).closest('.ps-popup').removeClass('active');
            $('body').css('overflow', 'auto');
        });
        $('#subscribe').on("click", function(event) {
            if (!$(event.target).closest(".ps-popup__content").length) {
                subscribe.removeClass('active');
                $("body").css('overflow-y', 'auto');
            }
        });
    }

    function stickySidebar() {
        var sticky = $('.ps-product--sticky'),
            stickySidebar, checkPoint = 992,
            windowWidth = $(window).innerWidth();
        if (sticky.length > 0) {
            stickySidebar = new StickySidebar('.ps-product__sticky .ps-product__info', {
                topSpacing: 20,
                bottomSpacing: 20,
                containerSelector: '.ps-product__sticky',
            });
            if ($('.sticky-2').length > 0) {
                var stickySidebar2 = new StickySidebar('.ps-product__sticky .sticky-2', {
                    topSpacing: 20,
                    bottomSpacing: 20,
                    containerSelector: '.ps-product__sticky',
                });
            }
            if (checkPoint > windowWidth) {
                stickySidebar.destroy();
                stickySidebar2.destroy();
            }
        } else {
            return false;
        }
    }

    function accordion() {
        var accordion = $('.ps-accordion');
        accordion.find('.ps-accordion__content').hide();
        $('.ps-accordion.active').find('.ps-accordion__content').show();
        accordion.find('.ps-accordion__header').on('click', function(e) {
            e.preventDefault();
            if ($(this).closest('.ps-accordion').hasClass('active')) {
                $(this).closest('.ps-accordion').removeClass('active');
                $(this).closest('.ps-accordion').find('.ps-accordion__content').slideUp(350);

            } else {
                $(this).closest('.ps-accordion').addClass('active');
                $(this).closest('.ps-accordion').find('.ps-accordion__content').slideDown(350);
                $(this).closest('.ps-accordion').siblings('.ps-accordion').find('.ps-accordion__content').slideUp();
            }
            $(this).closest('.ps-accordion').siblings('.ps-accordion').removeClass('active');
            $(this).closest('.ps-accordion').siblings('.ps-accordion').find('.ps-accordion__content').slideUp();
        });
    }

    function progressBar() {
        var progress = $('.ps-progress');
        progress.each(function(e) {
            var value = $(this).data('value');
            $(this).find('span').css({
                width: value + "%"
            })
        });
    }

    function customScrollbar() {
        $('.ps-custom-scrollbar').each(function() {
            var height = $(this).data('height');
            $(this).slimScroll({
                height: height + 'px',
                alwaysVisible: true,
                color: '#000000',
                size: '6px',
                railVisible: true,
            });
        })
    }

    function select2Cofig() {
        $('select.ps-select').select2({
            placeholder: $(this).data('placeholder'),
            minimumResultsForSearch: -1
        });
    }

    function carouselNavigation() {
        var prevBtn = $('.ps-carousel__prev'),
            nextBtn = $('.ps-carousel__next');
        prevBtn.on('click', function(e) {
            e.preventDefault();
            var target = $(this).attr('href');
            $(target).trigger('prev.owl.carousel', [1000]);
        });
        nextBtn.on('click', function(e) {
            e.preventDefault();
            var target = $(this).attr('href');
            $(target).trigger('next.owl.carousel', [1000]);
        });
    }

    function dateTimePicker() {
        $('.ps-datepicker').datepicker();
    }

    function jobDescriptionToggle() {
        var jobTitle = $('.ps-job__title');
        jobTitle.on('click', function(e) {
            e.preventDefault();
            $(this).closest('.ps-job').toggleClass('open');
            $(this).closest('.ps-job').find('.ps-job__desc').slideToggle(300);
        });

    }

    function imagesAnimations() {
        var imageLoadedSection = $('.ps-image-loaded'),
            targets = document.querySelectorAll('.ps-image-loaded .ps-animate'),
            effectSetting = {
                animeOpts: {
                    targets: targets,
                    duration: function(t, i) {
                        return 600 + i * 75;
                    },
                    easing: 'easeOutExpo',
                    delay: function(t, i) {
                        return i * 50;
                    },
                    opacity: {
                        value: [0, 1],
                        easing: 'linear'
                    },
                    scale: [0, 1]
                }
            };

        imageLoadedSection.imagesLoaded(function(e) {
            setTimeout(function() {
                imageLoadedSection.addClass('loaded');
                // if (effectSetting.revealer != undefined) {
                //     [].slice.call(targets).forEach(function(item) {
                //         var revealer = document.createElement('div');
                //         revealer.className = 'grid__reveal';
                //         if (effectSetting.revealerOrigin != undefined) {
                //             revealer.style.transformOrigin = effectSetting.revealerOrigin;
                //         }
                //         if (effectSetting.revealerColor != undefined) {
                //             revealer.style.backgroundColor = effectSetting.revealerColor;
                //         }
                //         item.parentNode.appendChild(revealer);
                //     });
                //
                //     var animeRevealerOpts = effectSetting.animeRevealerOpts;
                //     animeRevealerOpts.targets = document.querySelectorAll('.grid__reveal');
                //     animeRevealerOpts.begin = function(obj) {
                //         console.log(obj);
                //         for (var i = 0, len = obj.animatables.length; i < len; ++i) {
                //             obj.animatables[i].target.style.opacity = 1;
                //         }
                //     };
                //     anime.remove(animeRevealerOpts.targets);
                //     anime(effectSetting.animeRevealerOpts);
                // }
                anime(effectSetting.animeOpts)
            }, 500);
        });
    }

    function animateTestimonial() {
        var avatar = $('.ps-block--testimonials .ps-block__left a'),
            owl = $('.ps-block--testimonials').find('.owl-slider');
        owl.owlCarousel();
        avatar.on('click', function(e) {
            e.preventDefault();
            var el = $(this),
                position = el.index();
            if (!el.hasClass('active')) {
                el.addClass('active');
                el.siblings('a').removeClass('active');
                owl.trigger('to.owl.carousel', [position, 1, true]);
            }
        });
    }

    $(function() {
        backgroundImage();
        owlCarouselConfig();
        siteToggleAction();
        subMenuToggle();
        masonry('.ps-masonry');
        tabs();
        rating();
        stickyHeader();
        modalInit();
        searchInit();
        countDown();
        stickySidebar();
        accordion();
        progressBar();
        customScrollbar();
        select2Cofig();
        carouselNavigation();
        dateTimePicker();
        jobDescriptionToggle();
        imagesAnimations();
        animateTestimonial();
        new WOW().init();
    });

    $(window).on('load', function() {
        $('body').addClass('loaded');
        subscribePopup();
    });

})(jQuery);


