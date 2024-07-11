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


     // Add click event listener for btn1 to navigate to layout.html 
     var btn1 = document.getElementById('btn1');
     var btn2 = document.getElementById('btn2');
     var btn3 = document.getElementById('btn3');
     var btn4 = document.getElementById('btn4');
     var btn5 = document.getElementById('btn5');
     var editProfileBtn = document.getElementById('edit_profile');
     var editBoothBtn = document.getElementById('edit_booth');
     
     if (btn1) {
         btn1.addEventListener('click', function() {
             window.location.href = "/exhibition/list/";
         });
     }
     if (btn2) {
         btn2.addEventListener('click', function() {
             window.location.href = "/notice/";
         });
     }
     if (btn3) {
         btn3.addEventListener('click', function() {
             window.location.href = "/layout3/";
         });
     }
     if (btn4) {
         btn4.addEventListener('click', function() {
             window.location.href = "/FAQ/";
         });
     }
     if (btn5) {
        btn5.addEventListener('click', function() {
            window.location.href = "/exhibition/create_exhibition/";
        });
    }
     if (editProfileBtn) {
         editProfileBtn.addEventListener('click', function() {
             window.location.href = "/edit_profile/";
         });
     }
     if (editBoothBtn) {
         editBoothBtn.addEventListener('click', function() {
             window.location.href = "/edit_booth/";
         });
     }
});