// hidden input에서 년과 월에 대한 정보 가져오기
let year = document.querySelector('#year').value;
let months = document.querySelector('#months').value;
let day = document.querySelector('#day').value;
let stella = document.querySelector('#stella').value;

// 가져온 정보로 해당 월의 마지막날 찾기
let lastDateofMonth = new Date(year,months,0).getDate();

// 캘린더 완성에 필요한 다른 날들 찾기
let firstDayofMonth = new Date(year, months - 1, 1).getDay();
let lastDayofMonth = new Date(year, months - 1, lastDateofMonth).getDay();
let lastDateofLastMonth = new Date(year, months - 1, 0).getDate();

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
        li += `<li class = "inactive daaay before_month">${lastDateofLastMonth - i + 1}</li>`;
    }

    for (let i = 1; i <= lastDateofMonth; i++) {
        li += `<li class = "actives daaay">${i}</li>`;
	}

    for (let i = lastDayofMonth; i < 6; i++) {
        li += `<li class = "inactive daaay after_month">${i - lastDayofMonth + 1}</li>`;
     }
	daysTag.innerHTML = li;
 
}

// 지난달 화살표
const beforeMonths = () => {
    let year_month = "";
    if (months == 1) {
        let temp = parseInt(year) - 1;
        year_month = "" + String(temp) + "12";
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
    if (months == 12) {
        let temp = parseInt(year) + 1;
        year_month = "" + String(temp) + "01";
    } else {
        let new_month = parseInt(months) + 1;
        if (new_month < 10) {
            year_month = "" + year + "0" + new_month;
        } else {
            year_month = "" + year + new_month;
        }
    }
    window.location.href = '/mains/' + stella + "/" + year_month;
}

// 선택한 날짜에 대한 css 수정
const selectedDay = () => {
    if(day == 0)
        return 0;
    const lis = document.getElementsByClassName("actives");
    lis[day-1].classList.add("selected_day");
    lis[day-1].classList.remove("daaay");
}

const dayMove = (month_data,day_data) => {
    let year_month = "";
    if(month_data == "before"){
        if (months == 1) {
            let temp = parseInt(year) - 1;
            year_month = "" + String(temp) + "12";
        } else {
            let new_month = months - 1;
            if (new_month < 10) {
                year_month = "" + year + "0" + new_month;
            } else {
                year_month = "" + year + new_month;
            }
        }
    }
    else if(month_data == "after"){
        if (months == 12) {
            let temp = parseInt(year) + 1;
            year_month = "" + String(temp) + "01";
        } else {
            let new_month = parseInt(months) + 1;
            if (new_month < 10) {
                year_month = "" + year + "0" + new_month;
            } else {
                year_month = "" + year + new_month;
            }
        }
    }
    else{
        if (months < 10) {
            year_month = "" + year + "0" + months;
        } else {
            year_month = "" + year + months;
        }
    }

    window.location.href = '/mains/' + stella + "/" + year_month + "/" + day_data;
}

// 날짜 선택시 이동
const daySelect = () => {
    const day_list = document.getElementsByClassName("daaay");
    for(let i = 0 ; i < day_list.length ; i++){
        let month_data = "";
        if(day_list[i].classList.contains("before_month")){
            month_data = "before";
        }
        else if(day_list[i].classList.contains("after_month")){
            month_data = "after";
        }
        else{
            month_data = "now";
        }
        day_list[i].addEventListener('click',() => dayMove(month_data,day_list[i].innerHTML));
    }
}



////////////////// 이벤트 호출 및 등록하는 부분 /////////////////
renderCalendar();
selectedDay();
daySelect();
beforeMonthArrow.addEventListener('click',beforeMonths);
afterMonthArrow.addEventListener('click',afterMonths);

///////////////// a태그와 연결된 링크 수정 /////////////////
year_month = ""

if (months < 10) {
    year_month = "" + year + "0" + months;
} else {
    year_month = "" + year + months;
}

let a_link = document.getElementById('move-btn');
a_link.href = '/mains/' + stella + "/" + year_month + "/" + day + "/show";