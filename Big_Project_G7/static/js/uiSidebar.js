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
                        
                        // Create checkbox
                        let checkbox = document.createElement('input');
                        checkbox.type = 'checkbox';
                        checkbox.value = bookmark; // 체크박스의 값 설정 (북마크 이름)
                        checkbox.style.marginRight = '10px'; // 체크박스와 텍스트 사이 간격 설정
                        
                        // 북마크 상태 복원
                        let isChecked = JSON.parse(localStorage.getItem(bookmark)) || false;
                        checkbox.checked = isChecked;
                        
                        // 체크박스에 change 이벤트 리스너 추가
                        checkbox.addEventListener('change', function() {
                            localStorage.setItem(bookmark, checkbox.checked); // 상태 저장
                            updateTextDecoration(li, checkbox.checked); // 취소선 갱신
                        });
                        
                        // 리스트 아이템에 북마크 이름 추가
                        let label = document.createElement('label');
                        label.textContent = bookmark;
                        label.style.display = 'inline-block'; // 체크박스와 텍스트를 한 줄에 배치
                        label.style.verticalAlign = 'middle'; // 세로 정렬
                        label.style.textDecoration = isChecked ? 'line-through' : 'none'; // 초기 취소선 설정
                        
                        // 체크박스를 리스트 아이템에 추가
                        li.appendChild(checkbox);
                        li.appendChild(label);
                        
                        // 리스트 아이템을 modalBody에 추가
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

            
    // 텍스트에 취소선 스타일 적용/해제하는 함수
    function updateTextDecoration(element, isChecked) {
        if (isChecked) {
            element.querySelector('label').style.textDecoration = 'line-through';
        } else {
            element.querySelector('label').style.textDecoration = 'none';
        }
    }
});
