

// block-menu
const list = document.querySelectorAll('.btn');

function activeLink() {
	list.forEach((item) =>
	item.classList.remove('btn-1'));
	this.classList.add('btn-1');
}

list.forEach((item) =>
	item.addEventListener('click', activeLink));

// sidebar-profile
let openProfile = document.querySelector('.login-menu-js');
let btnOpen_profile = document.querySelector('.login');
let btnClose_onclick = document.querySelector('.header-adress');

btnOpen_profile.onclick = function() {
	openProfile.classList.toggle('login-menu');
}

btnClose_onclick.onclick = function() {
	openProfile.classList.remove('login-menu');
}

// adresses
let adress_list = document.querySelector('.adress-list');
let adressEvent = document.querySelector('.adress');

adressEvent.onmouseover = function showCard() {
	adress_list.style.display = 'block';
	adressEvent.onmouseout = function hideCard() {
		adress_list.style.display = 'none';
	}
}

// show menu for phones

let btnBar = document.querySelector('.show-all-menu')
let phonenavbarmenu = document.querySelector('.min-width-menu')
let bodyClass = document.querySelector('.body');

btnBar.onclick = function() {
	phonenavbarmenu.classList.toggle('min-width-menu-active');
	if(phonenavbarmenu.classList.contains('min-width-menu-active')) {
		bodyClass.style.overflow = 'hidden';
	} else {
		bodyClass.style.overflow = 'auto';
	}
}

// category filter
let btnCategory = document.querySelector('.categtory-filter-min-width');
let categoryList = document.querySelector('.upper-sidebar-min-width');
let arrowCategory = document.querySelector('.arrow-category')
btnCategory.onclick = function() {
	categoryList.classList.toggle('category-active');
	if(categoryList.classList.contains('category-active')) {
	arrowCategory.setAttribute('name', 'arrow-up-outline');
	} else {
		arrowCategory.setAttribute('name', 'arrow-down-outline');
	}
}