document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.floor-button');
    const floorInfos = {};

    buttons.forEach(button => {
        const floorNumber = button.getAttribute('data-floor');
        floorInfos[floorNumber] = {
            button: button,
            infos: document.querySelectorAll(`.floor-info.floor-${floorNumber}`)
        };

        button.addEventListener('click', () => {
            Object.values(floorInfos).forEach(floor => {
                floor.infos.forEach(info => info.style.display = 'none');
            });

            floorInfos[floorNumber].infos.forEach(info => {
                info.style.display = 'block';
            });
            buttons.forEach(btn => btn.classList.remove('on'));
            button.classList.add('on');
        });
    });

    // Initial display of 1층 정보
    const initialFloorNumber = '1';
    floorInfos[initialFloorNumber].infos.forEach(info => {
        info.style.display = 'block';
    });
    buttons.forEach(btn => {
        if (btn.getAttribute('data-floor') === initialFloorNumber) {
            btn.classList.add('on');
        }
    });
});
