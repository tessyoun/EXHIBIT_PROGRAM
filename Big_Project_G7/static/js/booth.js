document.addEventListener("DOMContentLoaded", function() {
    var searchButton = document.getElementById('search-button');
    var nameInput = document.getElementById('booth-name-input');
    var modal = document.getElementById("myModal");
    var closeButton = document.getElementsByClassName("close");
    var modalImage = document.getElementById("modalImage");
    var modalText0 = document.getElementById("modalText0");
    var modalText1 = document.getElementById("modalText1");
    var modalText2 = document.getElementById("modalText2");
    var suggestionsDiv = document.getElementById('suggestions');
    var categorySelect = document.querySelector('select[name="category"]');
    var rectangles = document.querySelectorAll('.rectangle');
    var selectedCategory = '전체';
    var bookmarkModal = document.getElementById("bookmarkModal");
    const reservationButton = document.getElementById('reservation');


    function populateCategories() {
        var categories = ['전체'];
        booths.forEach(function(booth) {
            var category = booth.fields.booth_category;
            if (!categories.includes(category)) {
                categories.push(category);
                var option = document.createElement('option');
                option.value = category;
                option.textContent = category;
                categorySelect.appendChild(option);
            }
        });

        var allOption = document.createElement('option');
        allOption.value = '전체';
        allOption.textContent = '전체';
        categorySelect.insertBefore(allOption, categorySelect.firstChild);
    }

    function filterRectangles(category) {
        rectangles.forEach(function(rectangle, index) {
            var booth = booths[index];
            if (booth && (category === '전체' || booth.fields.booth_category === category)) {
                rectangle.style.display = 'block';
            } else {
                rectangle.style.display = 'none';
            }
        });
    }

    function handleInput() {
        const userText = nameInput.value.trim().toLowerCase();
        suggestionsDiv.innerHTML = '';

        const filteredBooths = booths.filter(booth => {
            return (selectedCategory === '전체' || booth.fields.booth_category === selectedCategory) &&
                   booth.fields.booth_name.toLowerCase().includes(userText);
        });

        filteredBooths.forEach((booth, index) => {
            const suggestion = document.createElement('div');
            suggestion.classList.add('suggestion');
            suggestion.textContent = booth.fields.booth_name;
            suggestion.style.top = `${index * 40}px`;
            suggestion.addEventListener('click', function() {
                nameInput.value = booth.fields.booth_name;
                suggestionsDiv.innerHTML = '';
            });
            suggestionsDiv.appendChild(suggestion);
        });

        nameInput.addEventListener('click', function() {
            suggestionsDiv.style.display = 'block';
        });

        document.addEventListener('click', function(event) {
            if (!nameInput.contains(event.target)) {
                suggestionsDiv.style.display = 'none';
            }
        });
    }

    categorySelect.addEventListener('change', function() {
        selectedCategory = categorySelect.value.trim();
        filterRectangles(selectedCategory);
        handleInput();
    });

    populateCategories();
    categorySelect.selectedIndex = 0;
    filterRectangles(selectedCategory);
    nameInput.addEventListener('input', handleInput);

    if (searchButton) {
        searchButton.addEventListener('click', function() {
            const userText = nameInput.value.trim().toLowerCase();
            let found = false;

            for (let i = 0; i < booths.length; i++) {
                if (userText === booths[i].fields.booth_name.toLowerCase()) {
                    found = true;
                    const detectRect = document.querySelector(`.rectangle[data-index='${i}']`);
                    if (detectRect) {
                        detectRect.classList.add('blink');
                        setTimeout(() => detectRect.classList.remove('blink'), 5000);
                        detectRect.scrollIntoView({ behavior: "smooth", block: "center" });
                    }
                    break;
                }
            }
            if (!found) {
                alert("No matching booth found.");
            }
        });
    }

    function checkImageExists(url, callback) {
        var img = new Image();
        img.onload = function() { callback(true); };
        img.onerror = function() { callback(false); };
        img.src = url;
    }

    //창 생성
    function showModal(rectIndex) {
        const booth = booths[rectIndex];
        const boothId = booth.pk;
        const companyName = booth.fields.company_name;
        var result = booth.fields.company_name.slice(5, 8).replace(/[^0-9]/g, "");
        var formattedIndex = result.toString().padStart(2, '0');
        var imageName = booth.fields.company_name[0] + "_" + booth.fields.company_name.slice(3,5) + "_" + formattedIndex;

        var jpgImageName = imageName + ".jpg";
        var pngImageName = imageName + ".png";

        checkImageExists(imageBasePath + jpgImageName, function(exists) {
            if (exists) {
                modalImage.src = imageBasePath + jpgImageName;
            } else {
                checkImageExists(imageBasePath + pngImageName, function(exists) {
                    if (exists) {
                        modalImage.src = imageBasePath + pngImageName;
                    } else {
                        console.error('No image found for booth:', booth.booth_name);
                    }
                });
            }
        });

        // modalText.innerHTML = '<span class="modaltitle">기업명: </span>' + booth.fields.company_name +
        //                       '<br><span class="modaltitle">부스명: </span>' + booth.fields.booth_name +
        //                       '<br><span class="modaltitle">BM: </span>' + booth.fields.booth_category +
        //                       '<br> -' + booth.fields.background +
        //                       '<br> - ' + booth.fields.service;
        // modal.style.display = "block";

        modalText0.innerHTML = booth.fields.company_name;
        // 부스명, 기업명, BM
        modalText1.innerHTML ='<span class="modaltitle">' + booth.fields.booth_name + '</span>' +
                       '<br>' + booth.fields.booth_category;
                              
        // 설명
        modalText2.innerHTML = '<div>' +
                                '<span class="modaltitle">설명/서비스: </span>' +
                                '<br> - ' + booth.fields.background +
                                '<br> - ' + booth.fields.service +
                                '</div>';
        modal.style.display = "block";

        reservationButton.dataset.reservationUrl = `/booth_program/reserve/${boothId}/`;

        reservationButton.removeEventListener('click', handleReservation);
        reservationButton.addEventListener('click', handleReservation);
               // 북마크 버튼 클릭 시 처리
        let bookmarks = JSON.parse(localStorage.getItem('bookmarks')) || [];                     // #1 db로 저장경로 수정해야할 부분
        const bookmarkBtn = document.getElementById('bookmark-btn');
        bookmarkBtn.innerHTML = bookmarks.includes(boothId) ? '<i class="fa-solid fa-star fa-2x" style="color: #FFD43B;"> </i>' : '<i class="fa-regular fa-star fa-2x"> </i>';

        bookmarkBtn.addEventListener('click', function() {
            if (bookmarks.includes(boothId)) {
                // 북마크 취소
                bookmarks = bookmarks.filter(id => id !== boothId);
                bookmarkBtn.innerHTML = '<i class="fa-regular fa-star fa-2x"> </i>';
            } else {
                // 북마크 추가
                bookmarks.push(boothId);
                bookmarkBtn.innerHTML = '<i class="fa-solid fa-star fa-2x" style="color: #FFD43B;"> </i>';
            }
            localStorage.setItem('bookmarks', JSON.stringify(bookmarks));                       // #1 db로 저장경로 수정해야할 부분
            updateBookmarkIcons();
        });
    }

    //예약기능
    function handleReservation(event) {
        event.preventDefault();
        const companyName = encodeURIComponent(modalText0.innerText);
        if (companyName) {
            fetch(`/booth_program/check_program/${companyName}/`)
                .then(response => response.json())
                .then(data => {
                    if (data.exists) {
                        const reservationUrl = reservationButton.dataset.reservationUrl;
                        window.location.href = reservationUrl;
                    } else {
                        alert("기업에서 프로그램을 생성하지 않았습니다.");
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        } else {
            console.error('No company name found');
        }
    }
    
    //북마크 업데이트
    function updateBookmarkIcons() {
        let bookmarks = JSON.parse(localStorage.getItem('bookmarks')) || [];
        rectangles.forEach(function(rectangle, index) {
            if (!booths[index] || !booths[index].fields) return;
            const boothId = booths[index].pk;
            const existingIcon = rectangle.querySelector('.bookmark-icon');
            if (bookmarks.includes(boothId)) {
                if (!existingIcon) {
                    const starIcon = document.createElement('i');
                    starIcon.className = 'fa-solid fa-star bookmark-icon';
                    starIcon.style = 'color: #FFD43B;';
                    rectangle.appendChild(starIcon);
                }
            } else {
                if (existingIcon) {
                    rectangle.removeChild(existingIcon);
                }
            }
        });
        populateBookmarkOptions();
    }

    //스크롤기능
    const imageContainer = document.querySelector('.image-container');
    if (imageContainer) {
        const img = imageContainer.querySelector('img');

        let lastScrollX = 0;
        let lastScrollY = 0;

        imageContainer.addEventListener('scroll', function(event) {
            const deltaX = imageContainer.scrollLeft - lastScrollX;
            const deltaY = imageContainer.scrollTop - lastScrollY;

            lastScrollX = imageContainer.scrollLeft;
            lastScrollY = imageContainer.scrollTop;

            img.style.left = `${parseFloat(img.style.left) - deltaX}px`;
            img.style.top = `${parseFloat(img.style.top) - deltaY}px`;
        });
    } else {
        console.error("Element with class 'image-container' not found.");
    }

    //북마크 리스트
    function updateBookmarkModal() {
        let bookmarks = JSON.parse(localStorage.getItem('bookmarks')) || [];
        if (bookmarks.length > 0) {
            let bookmarkNames = booths.filter(booth => bookmarks.includes(booth.pk)).map(booth => booth.fields.booth_name);
            let modalBody = document.getElementById('bookmarkList');
            modalBody.innerHTML = ''; // Clear previous content
            
            bookmarkNames.forEach(function(bookmark) {
                let li = document.createElement('li');
                li.textContent = bookmark;
                modalBody.appendChild(li);
            });

            // Show modal
            bookmarkModal.style.display = 'block';
        } else {
            alert('북마크된 부스 없음.');
        }
    }

    // Event listener for showing bookmarks in modal
    const showBookmarksButton = document.getElementById('show-bookmarks');
    if (showBookmarksButton) {
        showBookmarksButton.addEventListener('click', function() {
            updateBookmarkModal();
        });
    }

    // 북마크 리셋
    const resetButton = document.getElementById('reset-bookmarks');
    resetButton.addEventListener('click', function() {
        bookmarks = [];
        localStorage.setItem('bookmarks', JSON.stringify(bookmarks));
        alert('북마크 리셋.');
        updateBookmarkIcons();
        clearLines();
    });
    
    //창 닫기 기능
    function closeModal() {
        modal.style.display = "none";
        bookmarkModal.style.display = "none";
    }

    document.querySelectorAll('.rectangle').forEach(function(rectangle, index) {
        rectangle.setAttribute('data-index', index);
        rectangle.addEventListener('click', function() {
            showModal(index);
        });
    });

    Array.from(closeButton).forEach(function(button) {
        button.addEventListener("click", closeModal);
    });

    window.onclick = function(event) {
        if (event.target === modal) {
            closeModal();
        }
        else if(event.target === bookmarkModal) {
            closeModal();
        }
    }

    updateBookmarkIcons();


    //경로 그리기
    const linesContainer = document.querySelector('.lines-container');

    function clearLines() {
        linesContainer.innerHTML = ''; // Clear lines by removing all child elements
    }

    function drawLinesBetweenBooths() {
        const startBoothId = document.getElementById('start_booth').value.trim();
        const endBoothId = document.getElementById('end_booth').value.trim();
    
        if (startBoothId === endBoothId) {
            alert('같은 부스를 선택하실 수 없습니다.');
            return; 
        }

        clearLines();
    
        linesContainer.innerHTML = ''; // Clear previous lines

        const startBooth = document.querySelector(`.rectangle[data-index='${startBoothId -1}']`);
        const endBooth = document.querySelector(`.rectangle[data-index='${endBoothId -1}']`);

        const startX = parseFloat(startBooth.dataset.centerX); 
        const startY = parseFloat(startBooth.dataset.centerY); 
        const endX = parseFloat(endBooth.dataset.centerX);  
        const endY = parseFloat(endBooth.dataset.centerY);   
    
        drawLine(startX, startY, endX, endY);
        startBooth.scrollIntoView({ behavior: "smooth", block: "center" });
    }

    function drawLine(startX, startY, endX, endY) {
        const line = document.createElement('div');
        line.classList.add('line');

        const length = Math.sqrt(Math.pow(endX - startX, 2) + Math.pow(endY - startY, 2));
        const angle = Math.atan2(endY - startY, endX - startX) * 180 / Math.PI;

        line.style.width = `${length}px`;
        line.style.height = '2px';
        line.style.left = `${startX}px`;
        line.style.top = `${startY}px`;
        line.style.position = 'absolute';
        line.style.transformOrigin = '0 0';
        line.style.transform = `rotate(${angle}deg)`;
        line.style.backgroundColor = 'black';
    
        linesContainer.appendChild(line);
    }
    
    //북마크 옵션 생성
    function populateBookmarkOptions() {
        let bookmarks = JSON.parse(localStorage.getItem('bookmarks')) || [];

        const startbookmarkSelect = document.getElementById('start_booth');
        const endbookmarkSelect = document.getElementById('end_booth');
        startbookmarkSelect.innerHTML = ''; // Clear previous options
        endbookmarkSelect.innerHTML = ''; // Clear previous options

        // Create an option for each bookmarked booth
        bookmarks.forEach(boothId => {
            const booth = booths.find(b => b.pk === boothId);
            if (booth) {
                const optionStart = document.createElement('option');
                const optionEnd = document.createElement('option');
                optionStart.value = booth.pk;
                optionStart.textContent = booth.fields.booth_name; // Adjust as per your booth data
                optionEnd.value = booth.pk;
                optionEnd.textContent = booth.fields.booth_name; // Adjust as per your booth data
                startbookmarkSelect.appendChild(optionStart);
                endbookmarkSelect.appendChild(optionEnd);
            }
        });
    }
    
    const drawLineButton = document.getElementById('draw-line-button');
    const eraseLineButton = document.getElementById('erase-route');

    if (drawLineButton) {
        drawLineButton.addEventListener('click', function() {
            drawLinesBetweenBooths();
        });
    }

    if (eraseLineButton) {
        eraseLineButton.addEventListener('click', function() {     
            clearLines();
        });
    }
});
