document.addEventListener("DOMContentLoaded", function() {
    var menuButton = document.querySelector('.header__button--menu');
    var sidebarBackdrop = document.querySelector('.sidebar__backdrop');
    var sidebarWrap = document.querySelector('.sidebar--wrap');  
    
    var accordionItems = document.querySelectorAll('.accordion-flush .accordion-item');
    
    accordionItems.forEach(function(item) {
        item.style.display = 'block'; // 'block' 으로 변경하여 보이게 설정
    });

    if (menuButton && sidebarBackdrop && sidebarWrap) {
        menuButton.addEventListener('click', function() {
            sidebarBackdrop.classList.add('visible');
            sidebarWrap.classList.add('visible');
            setTimeout(function() {
                sidebarWrap.classList.add('slide-in');
            }, 0); 
        });

        sidebarBackdrop.addEventListener('click', function() {
            sidebarWrap.classList.remove('slide-in');
            setTimeout(function() {
                sidebarBackdrop.classList.remove('visible');
                sidebarWrap.classList.remove('visible');
            }, 300); 
        });
    } else {
        console.error('One or more elements not found.');
    }

    // Modal close functionality
    const closeButtons = document.getElementsByClassName('close');
    const bookMModal = document.getElementById('bookMModal');

    // Sidebar bookmark list button event
    const sidebarShowBookmarksButton = document.getElementById('bookMlist');
    if (sidebarShowBookmarksButton) {
        sidebarShowBookmarksButton.addEventListener('click',  function() {
            let bookmarks = JSON.parse(localStorage.getItem('bookmarks')) || [];
            if (bookmarks.length > 0) {
                let bookmarkNames = booths.filter(booth => bookmarks.includes(booth.pk)).map(booth => booth.fields.booth_name);
                let modalBody = document.getElementById('bookmarkli');
                modalBody.innerHTML = ''; // Clear previous content
    
                bookmarkNames.forEach(function(bookmark) {
                    let li = document.createElement('li');
                    li.textContent = bookmark;
                    modalBody.appendChild(li);
                });
    
                bookMModal.style.display = 'block'; // Show modal
            } else {
                alert('북마크된 부스 없음.');
            }
        });
    }

    Array.from(closeButtons).forEach(function(btn) {
        btn.addEventListener('click', function() {
            bookMModal.style.display = 'none';
        });
    });


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