function toggleDetail(element) {
    const detailDiv = element.querySelector('.booth-detail');
    const editDiv = element.querySelector('.booth-edit');
    if (detailDiv.style.display === 'none') {
        detailDiv.style.display = 'block';
        editDiv.style.display = 'block';
    } else {
        detailDiv.style.display = 'none';
        editDiv.style.display = 'none';
    }
}
