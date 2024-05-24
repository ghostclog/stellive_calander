// 현재 URL 가져오기
const currentUrl = window.location.href;

// current-url 요소 가져오기
const currentUrlElement = document.getElementById("current-url");

// 일부 버튼들 기능
  document.getElementById('add-reply').addEventListener('click', function () {
    window.location.href = '/add/reply';
  });
  
  // 선택지 2 클릭 시 이벤트 처리
  document.getElementById('add-kiri').addEventListener('click', function () {
    window.location.href = '/add/clip';
  });

  document.getElementById('logo').addEventListener('click', function () {
    window.location.href = '/';
  });