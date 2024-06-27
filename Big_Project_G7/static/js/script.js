// 메뉴버튼, 챗봇 기능
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
            if (mobileMenu.style.display === "none" || mobileMenu.style.display === "") {
                mobileMenu.style.display = "block";
            } else {
                mobileMenu.style.display = "none";
            }
        });
    }

    if (chatIcon && chatContainer) {
        chatIcon.addEventListener('click', function() {
            chatContainer.classList.toggle('hidden');
        });
    }

    if (sendButton && userInput && chatBody) {
        sendButton.addEventListener('click', function() {
            const userText = userInput.value.trim();
            if (userText) {
                addUserMessage(userText);
                userInput.value = '';
                getBotResponse(userText);
            }
        });

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
            // Simulate a delay for bot response
            setTimeout(function() {
                const responses = {
                    "option1": "Response for option 1.",
                    "option2": "Response for option 2.",
                    "option3": "Response for option 3.",
                    "option4": "Response for option 4."
                };
                addBotMessage(responses[text] || "I'm not sure about that.");
            }, 1000);
        }

        // Handle option button clicks
        document.querySelectorAll('.option-button').forEach(function(button) {
            button.addEventListener('click', function() {
                addUserMessage(button.innerText);
                getBotResponse(button.innerText);
            });
        });
    }

    // Add click event listener for btn1 to navigate to layout.html 
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
});
