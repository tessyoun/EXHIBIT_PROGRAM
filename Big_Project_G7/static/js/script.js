document.addEventListener("DOMContentLoaded", function() {
    var menuBtn = document.getElementById("menu-btn");
    var mobileMenu = document.getElementById("mobile-menu");
    var sendButton = document.getElementById('send-button');
    var userInput = document.getElementById('user-input');
    var chatBody = document.getElementById('chat-body');
    var chatIcon = document.getElementById('chat-icon');
    var chatContainer = document.getElementById('chat-container');

    if (menuBtn && mobileMenu) {
        menuBtn.addEventListener("click", function() {
            mobileMenu.style.display = (mobileMenu.style.display === "none" || mobileMenu.style.display === "") ? "block" : "none";
        });
    }

    if (chatIcon && chatContainer) {
        chatIcon.addEventListener('click', function() {
            chatContainer.classList.toggle('hidden');
            if (!chatContainer.classList.contains('hidden') && !chatContainer.dataset.opened) {
                addBotMessage('안녕하세요! 무엇을 도와드릴까요?');
                chatContainer.dataset.opened = true;
            }
        });
    }

    if (sendButton && userInput && chatBody) {
        sendButton.addEventListener('click', sendMessage);

        userInput.addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                event.preventDefault();
                sendMessage();
            }
        });

        function sendMessage() {
            const userText = userInput.value.trim();
            if (userText) {
                addUserMessage(userText);
                userInput.value = '';
                getBotResponse(userText);
            }
        }

        function addUserMessage(text) {
            const userMessage = document.createElement('div');
            userMessage.classList.add('message', 'user-message');
            userMessage.innerHTML = `<p>${text}</p><span class="timestamp">${new Date().toLocaleTimeString()}</span>`;
            chatBody.appendChild(userMessage);
            chatBody.scrollTop = chatBody.scrollHeight;
        }

        function addBotMessage(text) {
            const botMessage = document.createElement('div');
            botMessage.classList.add('message', 'bot-message');
            botMessage.innerHTML = `<p>${text}</p><span class="timestamp">${new Date().toLocaleTimeString()}</span>`;
            chatBody.appendChild(botMessage);
            chatBody.scrollTop = chatBody.scrollHeight;
        }

        function getBotResponse(text) {
            fetch('/chatgpt/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ question: text })
            })
            .then(response => response.json())
            .then(data => {
                addBotMessage(data.result);
            })
            .catch(error => {
                console.error('Error:', error);
                addBotMessage("Sorry, there was an error processing your request.");
            });
        }

        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        document.querySelectorAll('.option-button').forEach(function(button) {
            button.addEventListener('click', function() {
                addUserMessage(button.innerText);
                getBotResponse(button.innerText);
            });
        });
    }

    var btn1 = document.getElementById('btn1');
    var btn2 = document.getElementById('btn2');
    var btn3 = document.getElementById('btn3');
    var btn4 = document.getElementById('btn4');
    var editProfileBtn = document.getElementById('edit_profile');
    var editBoothBtn = document.getElementById('edit_booth');

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
            window.location.href = "/layout4/";
        });
    }
    if (editProfileBtn) {
        editProfileBtn.addEventListener('click', function() {
            window.location.href = "/edit_profile/";
        });
    }
    if (editBoothBtn) {
        editBoothBtn.addEventListener('click', function() {
            window.location.href = "/edit_booth/";
        });
    }

    var modal = document.getElementById("myModal");
    var closeButton = document.getElementById("close-button");

    function showModal(rectIndex) {
        document.getElementById("modalText").innerText = "Rectangle " + rectIndex + " clicked!";
        modal.style.display = "block";
    }

    function closeModal() {
        modal.style.display = "none";
    }

    document.querySelectorAll('.rectangle').forEach(function(rectangle, index) {
        rectangle.addEventListener('click', function() {
            showModal(index);
        });
    });

    if (closeButton) {
        closeButton.addEventListener("click", closeModal);
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            closeModal();
        }
    }
});