let currentIndex = 0;
const slideTransitionDuration = 800;
const slideDisplayDuration = 3000;
const backgroundTransitionDuration = 800; 
let slideInterval;

document.addEventListener('DOMContentLoaded', function() {
    const slides = document.querySelector('.swiper--wrapper');
    const totalSlides = document.querySelectorAll('.exhibit__content').length;
    const slideWidth = document.querySelector('.exhibit__content').offsetWidth;
    const blurredBackground = document.querySelector('.blurred--background');

    function updateBackgroundImage(index) {
        blurredBackground.style.opacity = 0;

        setTimeout(() => {
            const slideImage = document.querySelectorAll('.poster__image')[index].src;
            blurredBackground.style.backgroundImage = `url(${slideImage})`;
            blurredBackground.style.opacity = 1;
        }, backgroundTransitionDuration / 2); 
    }

    function showSlide(index) {
        slides.style.transition = `transform ${slideTransitionDuration}ms ease-in-out`;
        slides.style.transform = `translateX(-${index * slideWidth}px)`;
        currentIndex = index;

        if (index >= totalSlides - 1) {
            setTimeout(() => {
                slides.style.transition = 'none';
                slides.style.transform = 'translateX(0)';
                currentIndex = 0;
                updateBackgroundImage(0);
            }, slideTransitionDuration);
        } else {
            updateBackgroundImage(index);
        }
    }

    function nextSlide() {
        showSlide(currentIndex + 1);
    }

    function startSlideShow() {
        slideInterval = setInterval(nextSlide, slideDisplayDuration);
    }

    function stopSlideShow() {
        clearInterval(slideInterval);
    }

    slides.addEventListener('mouseenter', stopSlideShow);
    slides.addEventListener('mouseleave', startSlideShow);

    updateBackgroundImage(0); 
    startSlideShow();
});