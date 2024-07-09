document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        locale: 'ko',  // 한국어로 설정
        selectable: true,
        select: function(info) {
            var selectedDate = info.startStr;
            document.getElementById('selected-date').textContent = '선택한 날짜: ' + selectedDate;
            fetchExhibitions(selectedDate);
        }
    });
    calendar.render();
});

function toggleCalendar() {
    var calendarContainer = document.getElementById('calendar-container');
    if (calendarContainer.style.display === 'none') {
        calendarContainer.style.display = 'block';
    } else {
        calendarContainer.style.display = 'none';
    }
}

function fetchExhibitions(selectedDate = '') {
    var url = selectedDate ? '/exhibition/list/' + selectedDate + '/' : '/exhibition/list/';
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            displayExhibitions(data);
        })
        .catch(error => console.error('Error:', error));
}

function displayExhibitions(exhibitions) {
    var exhibitionList = document.getElementById('exhibition-list');
    exhibitionList.innerHTML = '';
    
    if (exhibitions.length === 0) {
        exhibitionList.innerHTML = '<p>전시회가 없습니다.</p>';
    } else {
        exhibitions.forEach(function(exhibition) {
            var card = document.createElement('div');
            card.className = 'exhibition-card';
            card.onclick = function() {
                window.location.href = window.location.origin + '/' + exhibition.ExhibitionURL;
            };

            var name = document.createElement('h3');
            name.textContent = exhibition.ExhibitionName;

            var hallInfo = document.createElement('p');
            hallInfo.textContent = '전시장: ' + exhibition.Hall_ID__ExhibitionHallDescription;

            var dates = document.createElement('p');
            dates.textContent = '기간: ' + exhibition.ExhibitionRegistrationDate + ' ~ ' + exhibition.ExhibitionClosedDate;

            card.appendChild(name);
            card.appendChild(hallInfo);
            card.appendChild(dates);
            exhibitionList.appendChild(card);
        });
    }
}
