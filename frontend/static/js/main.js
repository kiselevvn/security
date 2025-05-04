(function ($) {
    "use strict";

    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);

        // Функция для плавного скроллинга
        function smoothScroll(target) {
            var $target = $(target);
            if ($target.length) {
                $('html, body').animate({
                    scrollTop: $target.offset().top
                }, 800);
            }
        }

        // Обработка клика по ссылкам с атрибутом href, начинающимся с #
        $('a[href^="#"]').on('click', function(event) {
            event.preventDefault(); // Отменяем стандартное поведение ссылки
            var target = this.hash; // Получаем id секции
            smoothScroll(target); // Плавный скроллинг до секции
            window.history.pushState(null, null, target); // Добавляем хэш в URL
        });

        // Проверка наличия хэша в URL при загрузке страницы
        if (window.location.hash) {
            smoothScroll(window.location.hash); // Плавный скроллинг до секции
        }
    });


    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });

    // Facts counter
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });

    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        center: true,
        autoplay: true,
        smartSpeed: 2000,
        dots: true,
        loop: true,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:3
            }
        }
    });
    $(document).ready(function(){
        $('#phone').mask('+7 (000) 000-00-00');
    });
})(jQuery);

