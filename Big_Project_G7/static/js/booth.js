document.addEventListener("DOMContentLoaded", function() {
    //booth search button
    var searchButton = document.getElementById('search-button');
    var nameInput = document.getElementById('booth-name-input');
    var modal = document.getElementById("myModal");
    var closeButton = document.getElementById("close-button");
    var modalImage = document.getElementById("modalImage");
    var modalText = document.getElementById("modalText");
    var suggestionsDiv = document.getElementById('suggestions');

    nameInput.addEventListener('input', function() {
        const userText = nameInput.value.trim().toLowerCase();
        suggestionsDiv.innerHTML = '';

        if (userText.length > 0) {
            const filteredBooths = booths_1st.filter(booth =>
                booth.fields.bname.toLowerCase().includes(userText) ||
                booth.fields.bcat.toLowerCase().includes(userText)
            );

            filteredBooths.forEach((booth, index) => {
                const suggestion = document.createElement('div');
                suggestion.classList.add('suggestion');
                suggestion.textContent = booth.fields.bname;
                suggestion.style.top = `${index * 40}px`; // Adjust the height as needed
                suggestion.addEventListener('click', function() {
                    nameInput.value = booth.fields.bname;
                    suggestionsDiv.innerHTML = ''; // Clear suggestions
                    highlightBooth(booth);
                });
                suggestionsDiv.appendChild(suggestion);
            });
        }
    });

    if (searchButton) {
        searchButton.addEventListener('click', function() {
            const userText = nameInput.value.trim().toLowerCase();
            let found = false;

            for (let i = 0; i < booths_1st.length; i++) {
                if (userText === booths_1st[i].fields.bname.toLowerCase() || userText === booths_1st[i].fields.bcat.toLowerCase()) {
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
        var result = booth.pk.slice(5, 8).replace(/[^0-9]/g, ""); //int 부분만 추출( 13조 -> 13 )
        var formattedIndex = result.toString().padStart(2, '0');
        var imageName = booth.pk[0] + "_" + booth.pk.slice(3,5) + "_" + formattedIndex;

        var jpgImageName = imageName + ".jpg";
        var pngImageName = imageName + ".png";

        checkImageExists(imageBasePath + jpgImageName, function(exists) {
            if (exists) {
                modalImage.src = imageBasePath + jpgImageName;
                modalText.innerText = "기업명: " + booth.pk + "\n부스명: " + booth.fields.bname + "\nBM: " + booth.fields.bcat + "\n설명: " + booth.fields.background + "\n서비스: " + booth.fields.service;
                modal.style.display = "block";
            } else {
                checkImageExists(imageBasePath + pngImageName, function(exists) {
                    if (exists) {
                        modalImage.src = imageBasePath + pngImageName;
                        modalText.innerText = "기업명: " + booth.pk + "\n부스명: " + booth.fields.bname + "\nBM: " + booth.fields.bcat + "\n설명: " + booth.fields.background + "\n서비스: " + booth.fields.service;
                        modal.style.display = "block";
                    } else {
                        console.error('No image found for booth:', booth.bname);
                    }
                });
            }
        });
        
    }

    function closeModal() {
        modal.style.display = "none";
    }

    document.querySelectorAll('.rectangle').forEach(function(rectangle, index) {
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
});