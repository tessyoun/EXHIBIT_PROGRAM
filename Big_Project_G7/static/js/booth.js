document.addEventListener("DOMContentLoaded", function() {
    //booth search button
    var searchButton = document.getElementById('search-button');
    var nameInput = document.getElementById('booth-name-input');
    var modal = document.getElementById("myModal");
    var closeButton = document.getElementById("close-button");
    var modalImage = document.getElementById("modalImage");
    var modalText = document.getElementById("modalText");
    var suggestionsDiv = document.getElementById('suggestions');
    var categorySelect = document.querySelector('select[name="category"]');
    var rectangles = document.querySelectorAll('.rectangle');
    var selectedCategory = '전체';
    const reservationButton = document.getElementById('reservation');

    // 카테고리 초기화
    function populateCategories() {
        var categories = ['전체'];
        booths_1st.forEach(function(booth) {
            var category = booth.fields.booth_category;
            if (!categories.includes(category)) {
                categories.push(category);
                var option = document.createElement('option');
                option.value = category;
                option.textContent = category;
                categorySelect.appendChild(option);
            }
        });
        
        // '전체' 카테고리 추가
        var allOption = document.createElement('option');
        allOption.value = '전체';
        allOption.textContent = '전체';
        categorySelect.insertBefore(allOption, categorySelect.firstChild); // 첫 번째 옵션으로 추가
    }

    // 사각형 필터링
    function filterRectangles(category) {
        rectangles.forEach(function(rectangle, index) {
            var booth = booths_1st[index];
            if (booth && (category === '전체' || booth.fields.booth_category === category)){
                rectangle.style.display = 'block';
            } else {
                rectangle.style.display = 'none';
            }
        });
    }

    // 부스 제안 필터링
    function handleInput() {
        const userText = nameInput.value.trim().toLowerCase();
        suggestionsDiv.innerHTML = '';

        const filteredBooths = booths_1st.filter(booth => {
            return (selectedCategory === '전체' || booth.fields.booth_category === selectedCategory) && // 선택된 카테고리와 일치
                   booth.fields.booth_name.toLowerCase().includes(userText); // 입력된 텍스트 포함
        });
        
        filteredBooths.forEach((booth, index) => {
            const suggestion = document.createElement('div');
            suggestion.classList.add('suggestion');
            suggestion.textContent = booth.fields.booth_name;
            suggestion.style.top = `${index * 40}px`; // 높이 조정
            suggestion.addEventListener('click', function() {
                nameInput.value = booth.fields.booth_name;
                suggestionsDiv.innerHTML = ''; // 제안 목록 초기화
            });
            suggestionsDiv.appendChild(suggestion);
        });
        // 입력 요소 클릭 시 제안 목록 보이기
        nameInput.addEventListener('click', function() {
            suggestionsDiv.style.display = 'block';
        });

        // 다른 곳 클릭 시 제안 목록 숨기기
        document.addEventListener('click', function(event) {
            if (!nameInput.contains(event.target)) {
                suggestionsDiv.style.display = 'none';
            }
        });

    }

    // 카테고리 선택 시 업데이트
    categorySelect.addEventListener('change', function() {
        selectedCategory = categorySelect.value.trim();
        filterRectangles(selectedCategory);
        handleInput(); // 카테고리 선택 시에도 제안 목록 업데이트
    });

    // 초기화 코드
    populateCategories();
    categorySelect.selectedIndex = 0; // '전체'를 기본 선택값으로 설정
    filterRectangles(selectedCategory); // 처음 로드 시 전체 부스 표시
    nameInput.addEventListener('input', handleInput);
    
    if (searchButton) {
        searchButton.addEventListener('click', function() {
            const userText = nameInput.value.trim().toLowerCase();
            let found = false;

            for (let i = 0; i < booths_1st.length; i++) {
                if (userText === booths_1st[i].fields.booth_name.toLowerCase()) {
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

    //booth click event
    console.log(booths_1st);
    console.log(booths_2nd);
    console.log(booths_3rd);
    console.log(booths_4th);
    
    function checkImageExists(url, callback) {
        var img = new Image();
        img.onload = function() { callback(true); };
        img.onerror = function() { callback(false); };
        img.src = url;
    }

    function showModal(rectIndex) {
        var booth = booths_1st[rectIndex - 1];
        var result = booth.fields.company_name.slice(5, 8).replace(/[^0-9]/g, ""); //int 부분만 추출( 13조 -> 13 )
        var formattedIndex = result.toString().padStart(2, '0');
        var imageName = booth.fields.company_name[0] + "_" + booth.fields.company_name.slice(3,5) + "_" + formattedIndex;

        var jpgImageName = imageName + ".jpg";
        var pngImageName = imageName + ".png";

        checkImageExists(imageBasePath + jpgImageName, function(exists) {
            if (exists) {
                modalImage.src = imageBasePath + jpgImageName;
                modalText.innerText = "기업명: " + booth.fields.company_name + "\n부스명: " + booth.fields.booth_name + "\nBM: " + booth.fields.booth_category + "\n설명: " + booth.fields.background + "\n서비스: " + booth.fields.service;
                modal.style.display = "block";
            } else {
                checkImageExists(imageBasePath + pngImageName, function(exists) {
                    if (exists) {
                        modalImage.src = imageBasePath + pngImageName;
                        modalText.innerText = "기업명: " + booth.fields.company_name + "\n부스명: " + booth.fields.booth_name + "\nBM: " + booth.fields.booth_category + "\n설명: " + booth.fields.background + "\n서비스: " + booth.fields.service;
                        modal.style.display = "block";
                    } else {
                        console.error('No image found for booth:', booth.booth_name);
                    }
                });
            }
        });
        //예약버튼
        reservationButton.addEventListener('click', function() {
            const reservationUrl = reservationButton.getAttribute('data-reservation-url').replace('placeholder_booth_id', booth.pk);
            window.location.href = reservationUrl;
        });
    }

    function closeModal() {
        modal.style.display = "none";
    }

    document.querySelectorAll('.rectangle').forEach(function(rectangle, index) {
        rectangle.setAttribute('data-index', index);
        rectangle.addEventListener('click', function() {
            showModal(index + 1);
        });
    });

    if (closeButton) {
        closeButton.addEventListener("click", closeModal);
    }

    window.onclick = function(event) {
        if (event.target === modal) {
            closeModal();
        }
    }

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
});