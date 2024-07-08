// uiScript.js

let currentCustomer = '개인';
let currentCategory = null;

const faqItems = document.querySelectorAll('.faq-item');
const categoryNav = document.getElementById('categoryNav');

const categories = {
    '개인': ['관람', '예약', '주차', '기타'],
    '기업': ['참가', '부스 설비', '주차', '기타']
};

function filterCustomer(customer) {
    currentCustomer = customer;
    currentCategory = null;
    updateCategoryNav();
    showFAQs();
}

function filterCategory(category) {
    currentCategory = category;
    showFAQs();
}

function updateCategoryNav() {
    categoryNav.innerHTML = '';
    categoryNav.style.display = 'block';
    const catLinks = categories[currentCustomer].map(cat => `<a href="javascript:void(0);" onclick="filterCategory('${cat}')">${cat}</a>`).join(' | ');
    categoryNav.innerHTML = catLinks;
}

function showFAQs() {
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
