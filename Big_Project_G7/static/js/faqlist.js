let currentCustomer = '개인';
let currentCategory = null;

const faqItems = document.querySelectorAll('.accordion-item');
const categoryNav = document.getElementById('categoryNav');

const categories = {
    '개인': ['전체', '관람', '예약', '주차', '기타'],
    '기업': ['전체', '참가', '부스 설비', '주차', '기타']
};

function filterCustomer(customer, element) {
    currentCustomer = customer;
    currentCategory = null;
    updateCategoryNav();
    updateFAQs();

    var items = document.querySelectorAll('.first-tag-item a');
    items.forEach(function(item) {
        item.classList.remove('on');
    });

    if (element) {
        element.classList.add('on');
    }
}

function filterCategory(category,element) {
    currentCategory = category === '전체' ? null : category;
    updateFAQs();

    const links = document.querySelectorAll('#categoryNav a');
    links.forEach(link => link.classList.remove('active'));

    if (element) {
        element.classList.add('active');
    }
}

function updateCategoryNav() {
    categoryNav.innerHTML = '';
    categoryNav.style.display = 'block';
    const catLinks = categories[currentCustomer].map(cat => `<a href="javascript:void(0);" onclick="filterCategory('${cat}', this)">${cat}</a>`).join(' | ');
    categoryNav.innerHTML = catLinks;
}

function updateFAQs() {
    const input = document.getElementById('searchInput').value.toUpperCase();
    faqItems.forEach(item => {
        const questionButton = item.querySelector('.accordion-button');
        const questionText = questionButton.innerText.toUpperCase();
        const customerMatch = item.getAttribute('data-customer') === currentCustomer;
        const categoryMatch = !currentCategory || item.getAttribute('data-category') === currentCategory;
        const searchMatch = questionText.indexOf(input) > -1;

        if (customerMatch && categoryMatch && searchMatch) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
}

function searchFAQs() {
    updateFAQs();
}


function toggleAnswer(element) {
    const answerDiv = element.querySelector('.answer');
    if (answerDiv.style.display === 'none') {
        answerDiv.style.display = 'block';
    } else {
        answerDiv.style.display = 'none';
    }
}

const defaultCustomerButton = document.querySelector('.first-tag-item a');
if (defaultCustomerButton) {
    filterCustomer(currentCustomer, defaultCustomerButton);
}