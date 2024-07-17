document.addEventListener('DOMContentLoaded', function() {
    const decreaseBtn = document.getElementById('decrease');
    const increaseBtn = document.getElementById('increase');
    const peopleCount = document.getElementById('people');
    const timeSlots = document.querySelectorAll('.time-slot');
    const reserveButton = document.getElementById('reserve-button');

    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

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
            if (!slot.classList.contains('disabled')) {
                timeSlots.forEach(s => s.classList.remove('selected'));
                slot.classList.add('selected');
            }
        });
    });

    // reserveButton.addEventListener('click', make_reservation);

    // function make_reservation() {
    //     const selectedTime = document.querySelector('.time-slot.selected').dataset.time;
    //     const people = document.getElementById('people').textContent;
    //     const boothCompanyName = '{{ booth.company_name }}';
    //     const boothName = '{{ booth.booth_name }}';

    //     $.ajax({
    //         type: 'POST',
    //         url: "{% url 'booth_program:submit_reservation' %}",
    //         data: {
    //             reserved_time: selectedTime,
    //             num_of_people: people,
    //             company_name: boothCompanyName,
    //             program_name: boothName,
    //             csrfmiddlewaretoken: csrfToken
    //         },
    //         success: function(response) {
    //             if (response.status === 'success') {
    //                 alert('예약 완료! 시간: ' + selectedTime + ', 인원수: ' + people);
    //                 window.location.href = "{% url 'booth_program:reservation_check' %}";
    //             } else {
    //                 alert('예약에 실패하였습니다.');
    //             }
    //         },
    //         error: function(xhr, status, error) {
    //             alert('AJAX 요청 실패: ' + error);
    //         }
    //     });
    // }
});
