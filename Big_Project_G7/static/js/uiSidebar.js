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
    const closeButtons = document.getElementsByClassName('BMclose');
    const bookMModal = document.getElementById('bookMModal');

    // Fetch booth information
    const boothUrl = "/get_booth_info/";  // Replace with your actual URL
    fetch(boothUrl)
        .then(response => response.json())
        .then(data => {
            const boothlist = JSON.parse(data);
            
            const sidebarShowBookmarksButton = document.getElementById('bookMlist');
            if (sidebarShowBookmarksButton) {
                sidebarShowBookmarksButton.addEventListener('click',  function() {
                    let bookmarks = JSON.parse(localStorage.getItem('bookmarks')) || [];
                    let bookmarkNames = boothlist.filter(booth => bookmarks.includes(booth.pk)).map(booth => booth.fields.booth_name);

                    let modalBody = document.getElementById('bookmarkli');
                    modalBody.innerHTML = ''; // Clear previous content

                    bookmarkNames.forEach(function(bookmark) {
                        let li = document.createElement('li');
                        li.textContent = bookmark;
                        modalBody.appendChild(li);
                    });

                    bookMModal.style.display = 'block'; // Show modal
                });
            }
        
            Array.from(closeButtons).forEach(function(btn) {
                btn.addEventListener('click', function() {
                    bookMModal.style.display = 'none';
                });
            });
        })
        .catch(error => console.error('Error fetching booth information:', error));

    //배치도 생성하면 display:none에서 block으로 변경
    if (localStorage.getItem('image_created') === 'true') {
        var createdLayItems = document.getElementsByClassName('created_lay');
        if (createdLayItems.length > 0) {
            createdLayItems[0].style.display = 'block'; // Show the sidebar menu item
        }
    }

});
