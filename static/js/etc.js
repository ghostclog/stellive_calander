  // 선택지 1 클릭 시 이벤트 처리
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