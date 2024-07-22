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
             window.location.href = "/AIVEX/about/";
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

    

     

    //  pc 포스터 슬라이드
    $(document).ready(function() {
        function moveToSelected(element) {
            var selected;
    
            if (element == "next") {
                selected = $(".selected").next();
                if (selected.length === 0) {
                    selected = $("#carousel div").first();
                }
            } else if (element == "prev") {
                selected = $(".selected").prev();
                if (selected.length === 0) {
                    selected = $("#carousel div").last();
                }
            } else {
                selected = element;
            }
    
            var next = $(selected).next();
            var prev = $(selected).prev();
            var prevSecond = $(prev).prev();
            var nextSecond = $(next).next();
    
            $("#carousel div").removeClass().addClass('hide'); // 기본적으로 모든 슬라이드를 숨김
            $(selected).removeClass('hide').addClass("selected");
            $(prev).removeClass('hide').addClass("prev");
            $(next).removeClass('hide').addClass("next");
            $(nextSecond).removeClass('hide').addClass("nextRightSecond");
            $(prevSecond).removeClass('hide').addClass("prevLeftSecond");
            $(nextSecond).nextAll().removeClass().addClass('hideRight');
            $(prevSecond).prevAll().removeClass().addClass('hideLeft');
    
            var slideText = $(selected).data("text");
            updateSlideText(slideText);
        }
    
        function updateSlideText(text) {
            var slideTextDiv = $("#slide-text");
            slideTextDiv.removeClass('show'); // 텍스트 숨기기
    
            // 잠시 대기 후 텍스트 업데이트
            setTimeout(function() {
                slideTextDiv.html(text); // 텍스트 설정
                slideTextDiv.addClass('show'); // 텍스트 보이기
            }, 500); // 페이드 아웃 후 500ms 대기
        }
    
        $(document).keydown(function(e) {
            switch (e.which) {
                case 37: // Left arrow key
                    moveToSelected('prev');
                    break;
                case 39: // Right arrow key
                    moveToSelected('next');
                    break;
                default:
                    return;
            }
            e.preventDefault();
        });
    
        $('#carousel div').click(function() {
            moveToSelected($(this));
        });
    
        $('#prev').click(function() {
            moveToSelected('prev');
        });
    
        $('#next').click(function() {
            moveToSelected('next');
        });
    
        setInterval(function() {
            moveToSelected('next');
        }, 4000); // 4초마다 자동 슬라이드
    });
    
    
    



    var btn1PC = document.getElementById('btn1-pc');
     var btn2PC = document.getElementById('btn2-pc');
     var btn3PC = document.getElementById('btn3-pc');
     var btn4PC = document.getElementById('btn4-pc');
     var btn5PC = document.getElementById('btn5-pc');

     
    if (btn1PC) {
        btn1PC.addEventListener('click', function() {
            window.location.href = "/exhibition/list/";
        });
    }
    if (btn2PC) {
        btn2PC.addEventListener('click', function() {
            window.location.href = "/notice/";
        });
    }
    if (btn3PC) {
        btn3PC.addEventListener('click', function() {
            window.location.href = "/AIVEX/about/";
        });
    }
    if (btn4PC) {
        btn4PC.addEventListener('click', function() {
            window.location.href = "/FAQ/";
        });
    }
    if (btn5PC) {
        btn5PC.addEventListener('click', function() {
            window.location.href = "/exhibition/create_exhibition/";
        });
    }
});