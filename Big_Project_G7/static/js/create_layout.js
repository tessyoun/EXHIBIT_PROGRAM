function downloadImage(imageData, fileName) {
    const link = document.createElement('a');
    link.href = imageData;
    link.download = fileName;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

function handleImageClick(event) {
    const imageData = event.target.src;
    const fileName = `image_${Date.now()}.png`;
    downloadImage(imageData, fileName);
}

document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('.generated-image');
    images.forEach(image => {
        image.addEventListener('click', handleImageClick);
    });
});