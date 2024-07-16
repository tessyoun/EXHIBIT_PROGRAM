document.addEventListener('DOMContentLoaded', function() {
    const decreaseBtn = document.getElementById('decrease');
    const increaseBtn = document.getElementById('increase');
    const peopleCount = document.getElementById('people');
    const timeSlots = document.querySelectorAll('.time-slot');
    const reserveButton = document.getElementById('reserve-button');

    decreaseBtn.addEventListener('click', () => {
        let count = parseInt(peopleCount.textContent);
        if (count > 1) {
            peopleCount.textContent = count - 1;
        }
    });

    increaseBtn.addEventListener('click', () => {
        let count = parseInt(peopleCount.textContent);
        peopleCount.textContent = count + 1;
    });

    timeSlots.forEach(slot => {
        slot.addEventListener('click', () => {
            timeSlots.forEach(s => s.classList.remove('selected'));
            slot.classList.add('selected');
        });
    });

    reserveButton.addEventListener('click', () => {
        const selectedTime = document.querySelector('.time-slot.selected').dataset.time;
        const people = peopleCount.textContent;
        const boothCompanyName = document.querySelector('.booth-info p:nth-child(1)').textContent.split(': ')[1];
        const boothName = document.querySelector('.booth-info p:nth-child(2)').textContent.split(': ')[1];

        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        fetch('/booth_program/submit_reservation/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrfToken
            },
            body: new URLSearchParams({
                'program_name': boothName,
                'num_of_people': people,
                'reserved_time': selectedTime
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                alert('예약 완료! 시간: ' + selectedTime + ', 인원수: ' + people);
                window.location.href = '/booth_program/reservation_check/';
            } else {
                alert('예약 실패: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('예약 중 오류가 발생했습니다.');
        });
    });
});