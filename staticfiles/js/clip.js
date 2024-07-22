// 클립 탭 닫는 이벤트
function handleButtonClick(event) {
    // 클릭한 버튼
    let clickedButton = event.target;

    // 클릭한 버튼의 부모의 부모인 clip-box 요소 찾기
    let clipBox = event.target.closest('.clip-box');

    // clipBox가 지니고 있는 두 번째 자식인 clip-vedio를 찾기
    let clipVedio = clipBox.querySelector('.clip-vedio');

    // 클립 탭 상태 추적 변수
    let isClipOpen = clipVedio.style.paddingBottom === '56.25%';

    // 클립 탭이 열려있으면 닫고, 닫혀있으면 열기
    clipVedio.style.paddingBottom = isClipOpen ? '0' : '56.25%';
    clickedButton.style.transform = isClipOpen ? 'rotate(0deg)' : 'rotate(90deg)';
}

// clip-btn 클래스에 이벤트 등록
let clipBtns = document.querySelectorAll('.clip-btn');
clipBtns.forEach(function (btn) {
    btn.addEventListener('click', handleButtonClick);
});