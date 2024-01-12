// hidden input에서 년과 월에 대한 정보 가져오기
let year = document.querySelector('#year').value;
let months = document.querySelector('#months').value;
let stella = document.querySelector('#stella').value;

// 가져온 정보로 해당 월의 마지막날 찾기
let lastDateofMonth = new Date(year,months,0).getDate();

// 캘린더 완성에 필요한 다른 날들 찾기
let firstDayofMonth = new Date(year, months - 1, 1).getDay();
let lastDayofMonth = new Date(year, months - 1, lastDateofMonth).getDay();
let lastDateofLastMonth = new Date(year, months - 2, 0).getDate();

// 이벤트가 발생할 div들
// 캘린더 화살표
let beforeMonthArrow = document.querySelector('#beforeMonthArrow');
let afterMonthArrow = document.querySelector('#afterMonthArrow');

// 캘린더 내부의 데이터 수정
let daysTag = document.querySelector('.days');


/////////////////////// 이벤트와 메소드 구현 부분 /////////////////////
// 캘린더 그리기
const renderCalendar = () => {
    let li = '';
    for (let i = firstDayofMonth; i > 0; i--) {
        li += `<li class = "inactive">${lastDateofLastMonth - i + 1}</li>`;
    }

    for (let i = 1; i <= lastDateofMonth; i++) {
        li += `<li>${i}</li>`;
	}

    for (let i = lastDayofMonth; i < 6; i++) {
        li += `<li class = "inactive">${i - lastDayofMonth + 1}</li>`;
     }
	daysTag.innerHTML = li;
 
}

// 에러 발생. 해결해야함.
// 지난달 화살표
const beforeMonths = () => {
    let year_month = "";
    if (months === 1) {
        let temp = year - 1;
        year_month = "" + temp + "12";
    } else {
        let new_month = months - 1;
        if (new_month < 10) {
            year_month = "" + year + "0" + new_month;
        } else {
            year_month = "" + year + new_month;
        }
    }
    window.location.href = '/mains/' + stella + "/" + year_month;
}

// 다음달 화살표
const afterMonths = () => {
    let year_month = "";
    if (months === 12) {
        let temp = year + 1;
        year_month = "" + temp + "01";
    } else {
        let new_month = months + 1;
        if (new_month < 10) {
            year_month = "" + year + "0" + new_month;
        } else {
            year_month = "" + year + new_month;
        }
    }
    window.location.href = '/mains/' + stella + "/" + year_month;
}


////////////////// 이벤트 호출 및 등록하는 부분 /////////////////
renderCalendar();
beforeMonthArrow.addEventListener('click',beforeMonths);
afterMonthArrow.addEventListener('click',afterMonths);