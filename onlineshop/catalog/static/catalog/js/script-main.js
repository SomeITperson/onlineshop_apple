// images changing

let imageList = ['main2.png', 'main3.png', 'main1.png'];
let length = imageList.length;
let index = 0;

window.onload = function() {
	setInterval(function() {
		if(length == index) {
			index = 0;
		}
		document.querySelector('.animated-pictures').src = `static/catalog/images/${imageList[index++]}`;
	}, 10000)
}


// words value in input

const textarea = document.querySelector('.textarea');
let result = document.querySelector('.result');
const btnSubmit = document.querySelector('.button-send');
const limit = 120;

function checkTextarea() {
	result.textContent = 0 + '/' + limit

	textarea.addEventListener('input', () => {
		const textLength = textarea.value.length;
		result.textContent = textLength + '/' + limit;
	})

	if(result>limit) {
		btnSubmit.disabled = true;
	}else {
		btnSubmit.disabled = false;
	}
}

checkTextarea ();

// chat
// let btn = document.querySelector('.callback-btn');
// let content = document.querySelector('.callback');
// let changeImg = document.querySelector('.active');

// btn.onclick = function() {
// 	content.classList.toggle('active');
// 	btn.classList.toggle('active_btn');
// 	let chatImg = document.querySelector('.icon-msg');
// 	chatImg.setAttribute('name', 'add-outline');
// 	if(!content.classList.contains('active')) {
// 		chatImg.setAttribute('name', 'chatbubble-ellipses-outline');
// 	}
// }

// callback

// let changeField = document.getElementById('user-name');

// changeField.onfocus = function() {
// 	changeField.setAttribute('value', '');
// 	changeField.removeAttribute('readonly');
// }