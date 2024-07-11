document.addEventListener("DOMContentLoaded", function() {
        var observer = new MutationObserver(function(mutationsList, observer) {
            var menuButton = document.querySelector('.header__button--menu');
            var sidebarBackdrop = document.querySelector('.sidebar__backdrop');
            var sidebarWrap = document.querySelector('.sidebar--wrap');
            var homeButton = document.querySelector('.sidebar__menu--home');

            console.log('Menu Button:', menuButton);
console.log('Sidebar Backdrop:', sidebarBackdrop);
console.log('Sidebar Wrap:', sidebarWrap);
console.log('Home Button:', homeButton);

    if (menuButton && sidebarBackdrop && sidebarWrap && homeButton) {
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

        sidebarBackdrop.addEventListener('click', function() {
            sidebarBackdrop.classList.remove('visible');
            sidebarWrap.classList.remove('slide-in');
            setTimeout(function() {
                sidebarWrap.classList.remove('visible');
            }, 300); 
        });
    } else {
        console.error('One or more elements not found.');
    }

    // // Example code for handling bookmarks
    // const listButton = document.getElementById('personal-bookmarks');
    // if (listButton) {
    //     listButton.addEventListener('click', function() {
    //         let bookmarks = JSON.parse(localStorage.getItem('bookmarks')) || [];
    //         if (bookmarks.length > 0) {
    //             // Replace with your logic to handle bookmarks
    //             alert('북마크 부스: \n\n' + bookmarks.join('\n'));
    //         } else {
    //             alert('북마크된 부스 없음.');
    //         }
    //     });
    // } else {
    //     console.error('Personal bookmarks button not found.');
    // }
});
observer.observe(document.body, { childList: true, subtree: true });
});
