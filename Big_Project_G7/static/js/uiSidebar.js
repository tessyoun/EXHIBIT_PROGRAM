document.addEventListener("DOMContentLoaded", function() {
    var menuButton = document.querySelector('.header__button--menu');
    var sidebarBackdrop = document.querySelector('.sidebar__backdrop');
    var sidebarWrap = document.querySelector('.sidebar--wrap');
    var homeButton = document.querySelector('.sidebar__menu--home')

    if (menuButton && sidebarBackdrop && sidebarWrap) {
        menuButton.addEventListener('click', function() {
            sidebarBackdrop.classList.add('visible');
            sidebarWrap.classList.add('visible');
            setTimeout(function() {
                sidebarWrap.classList.add('slide-in');
            }, 0); 
        });

        homeButton.addEventListener('click', function() {
            sidebarBackdrop.classList.remove('visible');
            sidebarWrap.classList.remove('slide-in');
            setTimeout(function() {
                sidebarWrap.classList.remove('visible');
            }, 300); 
        });
    }
});
