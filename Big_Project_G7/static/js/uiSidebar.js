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

        // 바깥에 검은 영역 클릭 시에도 닫힘
        sidebarBackdrop.addEventListener('click', function() {
            sidebarBackdrop.classList.remove('visible');
            sidebarWrap.classList.remove('slide-in');
            setTimeout(function() {
                sidebarWrap.classList.remove('visible');
            }, 300); 
        });
    }
    //북마크
    const listButton = document.getElementById('personal-bookmarks');
    listButton.addEventListener('click', function() {
        let bookmarks = JSON.parse(localStorage.getItem('bookmarks')) || [];
        if (bookmarks.length > 0) {
            let bookmarkNames = booths.filter(booth => bookmarks.includes(booth.fields.company_id)).map(booth => booth.fields.booth_name);
            alert('북마크 부스: \n\n' + bookmarkNames.join('\n'));
        } else {
            alert('북마크된 부스 없음.');
        }
    });
});
