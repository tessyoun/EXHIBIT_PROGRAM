document.addEventListener('DOMContentLoaded', function() {

    // 챗봇 버튼 클릭시 행동 구현
    const chatbotToggle = document.getElementById('chatbotToggle');
    const chatbotWindow = document.getElementById('chatbotWindow');
    let isOpen = false;

    chatbotToggle.addEventListener('click', function() {
        isOpen = !isOpen;

        if (isOpen) {
            chatbotWindow.style.display = 'block';
            chatbotToggle.style.backgroundImage = 'url("../static/icons/chatbot_close.png")';
        } else {
            chatbotWindow.style.display = 'none';
            chatbotToggle.style.backgroundImage = 'url("../static/icons/chatbot_icon.png")';
        }
    });


    // 채팅 구현
    var sendButton = document.getElementById('send-button');
    var userInput = document.getElementById('message--input');
    var chatBody = document.getElementById('chatbot__body');

    if (sendButton && userInput && chatBody) {
        sendButton.addEventListener('click', function() {
            sendMessage();
        });

        userInput.addEventListener('keydown', function(event) {
            if (event.key === 'Enter' && !event.shiftKey) {
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
            const currentTime = new Date();
            const timeString = formatTime(currentTime.getHours(), currentTime.getMinutes());
            userMessage.innerHTML = `<div class="message-content">${text}</div><span class="timestamp">${timeString}</span>`;
            chatBody.appendChild(userMessage);
            chatBody.scrollTop = chatBody.scrollHeight;
        }
        
        function addBotMessage(text) {
            const botMessage = document.createElement('div');
            botMessage.classList.add('message', 'bot-message');
            const currentTime = new Date();
            const timeString = formatTime(currentTime.getHours(), currentTime.getMinutes());
            botMessage.innerHTML = `<img class="bot-profile"><div class="message-content">${text}</div><span class="timestamp">${timeString}</span>`;
            chatBody.appendChild(botMessage);
            chatBody.scrollTop = chatBody.scrollHeight;
        }
        
        // 시간을 HH:MM 으로 표시
        function formatTime(hours, minutes) {
            const formattedHours = hours < 10 ? `0${hours}` : hours;
            const formattedMinutes = minutes < 10 ? `0${minutes}` : minutes;
            return `${formattedHours}:${formattedMinutes}`;
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
