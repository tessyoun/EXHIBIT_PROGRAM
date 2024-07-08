document.addEventListener('DOMContentLoaded', function() {
    const icon = document.getElementById('pw-info-icon');
    const helptext = document.getElementById('id_password1_helptext');
    const iconElement = icon.querySelector('i');
    
    icon.addEventListener('mouseover', function() {
        helptext.style.display = 'block';
        iconElement.style.color = '#5f5f5f';
    });
    
    icon.addEventListener('mouseout', function() {
        helptext.style.display = 'none';
        iconElement.style.color = '#bebebe';
    });
});