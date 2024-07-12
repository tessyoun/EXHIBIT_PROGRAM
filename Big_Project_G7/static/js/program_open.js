document.addEventListener("DOMContentLoaded", function() {
    var menuButton = document.querySelector('.header__button--menu');
    var sidebarBackdrop = document.querySelector('.sidebar__backdrop');
    var sidebarWrap = document.querySelector('.sidebar--wrap');
    var homeButton = document.querySelector('.sidebar__menu--home');

    if (menuButton && sidebarBackdrop && sidebarWrap) {
        menuButton.addEventListener('click', function() {
            sidebarBackdrop.classList.add('visible');
            sidebarWrap.classList.add('visible');
            setTimeout(function() {
                sidebarWrap.classList.add('slide-in');
            }, 0); 
        });

        if (homeButton) {
            homeButton.addEventListener('click', function() {
                sidebarBackdrop.classList.remove('visible');
                sidebarWrap.classList.remove('slide-in');
                setTimeout(function() {
                    sidebarWrap.classList.remove('visible');
                }, 300); 
            });
        }
    }

    var selectedTimes = [];
    document.querySelectorAll(".time-slot").forEach(function(slot) {
        slot.addEventListener("change", function() {
            var time = slot.value;
            if (slot.checked) {
                if (!selectedTimes.includes(time)) {
                    selectedTimes.push(time);
                }
            } else {
                selectedTimes = selectedTimes.filter(function(t) { return t !== time; });
            }
            document.getElementById("selected-times").value = selectedTimes.join(",");
            console.log("Selected times:", selectedTimes);
        });
    });

    var btn1 = document.getElementById('btn1');
    var btn2 = document.getElementById('btn2');
    var btn3 = document.getElementById('btn3');
    var btn4 = document.getElementById('btn4');
    var btn5 = document.getElementById('btn5');
    
    if (btn1) {
        btn1.addEventListener('click', function() {
            window.location.href = "/layout1/";
        });
    }
    if (btn2) {
        btn2.addEventListener('click', function() {
            window.location.href = "/layout2/";
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
            window.location.href = "/layout5/";
        });
    }
});
