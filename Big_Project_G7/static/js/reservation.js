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

});