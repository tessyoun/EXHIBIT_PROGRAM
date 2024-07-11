let currentCustomer = '개인';
let currentCategory = null;

const faqItems = document.querySelectorAll('.accordion-item');
const categoryNav = document.getElementById('categoryNav');

const categories = {
    '개인': ['관람', '예약', '주차', '기타'],
    '기업': ['참가', '부스 설비', '주차', '기타']
};

function filterCustomer(customer, element) {
    currentCustomer = customer;
    currentCategory = null;
    updateCategoryNav();
    showFAQs();

    var items = document.querySelectorAll('.first-tag-item a');
    items.forEach(function(item) {
        item.classList.remove('on');
    });

    element.classList.add('on');
}

function filterCategory(category) {
    currentCategory = category;
    showFAQs();

    const links = document.querySelectorAll('#categoryNav a');
    links.forEach(link => link.classList.remove('active'));

    element.classList.add('active');
}

function updateCategoryNav() {
    const categoryNav = document.getElementById('categoryNav');
    categoryNav.innerHTML = '';
    categoryNav.style.display = 'block';
    const catLinks = categories[currentCustomer].map(cat => `<a href="javascript:void(0);" onclick="filterCategory('${cat}', this)">${cat}</a>`).join(' | ');
    categoryNav.innerHTML = catLinks;
}

function showFAQs() {
    const faqItems = document.querySelectorAll('.accordian-item');
    faqItems.forEach(item => {
        const customerMatch = item.getAttribute('data-customer') === currentCustomer;
        const categoryMatch = !currentCategory || item.getAttribute('data-category') === currentCategory;
        if (customerMatch && categoryMatch) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
}

function searchFAQs() {
    const input = document.getElementById('searchInput').value.toUpperCase();
    faqItems.forEach(item => {
        const question = item.querySelector('.question-summary').innerText.toUpperCase();
        if (question.indexOf(input) > -1 && item.getAttribute('data-customer') === currentCustomer && (!currentCategory || item.getAttribute('data-category') === currentCategory)) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
}

function toggleAnswer(element) {
    const answerDiv = element.querySelector('.answer');
    if (answerDiv.style.display === 'none') {
        answerDiv.style.display = 'block';
    } else {
        answerDiv.style.display = 'none';
    }
}

filterCustomer(currentCustomer);
