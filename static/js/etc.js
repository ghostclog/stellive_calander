window.onload = function() {
    const errorMessage = sessionStorage.getItem('error_message');

    if (errorMessage) {
        alert(errorMessage);
        sessionStorage.removeItem('error_message');  // 경고 후 세션 삭제
    }
};

// 모달 열기 버튼 클릭 시 이벤트 처리
document.getElementById('add-data').addEventListener('click', function () {
    document.getElementById('clip-Modal').style.display = 'block';
    document.getElementById('modal-back').style.display = 'block';
  });
  
  // 선택지 1 클릭 시 이벤트 처리
  document.getElementById('option1').addEventListener('click', function () {
    window.location.href = '/add/reply';
  });
  
  // 선택지 2 클릭 시 이벤트 처리
  document.getElementById('option2').addEventListener('click', function () {
    window.location.href = '/add/clip';
  });

  document.getElementById('option3').addEventListener('click', function () {
    document.getElementById('clip-Modal').style.display = 'none';
    document.getElementById('modal-back').style.display = 'none';
  });
  