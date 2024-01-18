from django.shortcuts import render,redirect
from datetime import datetime
from . import models,forms



# 메인 페이지1(스텔라 선택 전.)
def main_page(request):
    if request.method == "GET":
        formatted_date = datetime.now().strftime('%B %Y')
        return render(request,"page.html",{'string_date' : formatted_date})
    
# 메인 페이지2(스텔라 선택 후. 캘린더는 최신 연월로 설정 / 캘린더에 방송 한 날짜 굵게 표시)
def stella_default_page(request,stella):
    if request.method == "GET":
        year = str(datetime.now().year)
        month = str(datetime.now().month)
        redirect_url = "/mains/" + stella + "/" + year + month.zfill(2)
        return redirect(redirect_url)

# 메인 페이지3(스텔라 선택. 연월 선택 시 / 캘린더에 방송 한 날짜 굵게 표시)
def stella_date_page(request,stella,date):
    if request.method == "GET":
        # 날짜 정보
        year = int(date[0:4])
        month = int(date[4:])

        try: # 연 월 데이터 잘못 입력시
            formatted_date = datetime(year, month, 1).strftime('%B %Y')
        except:
            return redirect("/mains/")

        try:
            # stella변수. 코드에서 이름으로 변환 / 스텔라 이름 잘못 입력시
            stella_name = models.Stellas.objects.get(stella_name_code = stella)
        except:
            return redirect("/mains/")
        
        #bangsong_day = list(models.Replay.objects.filter(stella = stella_name, replay_day__year=year, replay_day__month=month))


        return render(request,"members.html",
                      { 'stella': stella,
                        'string_date' : formatted_date,
                        'stella_name' : stella_name,
                        'total_date_data' : "아직 날짜가 설정되지 않았습니다.",
                        'contents' : "아직 날짜가 설정되지 않았습니다.",
                        'clips' : "아직 날짜가 설정되지 않았습니다.",
                        'for_calander_date':[year,month,0],})
                        #'bangsong_day' : bangsong_day})
    
# 메인 페이지3(날짜 선택 / 캘린더에 방송 한 날짜 굵게 표시 + 정보창에 정보 띄우기)
def stella_detail_page(request,stella,date,day):
    if request.method == "GET":

        # 일자를 잘못 입력 한 경우.
        if(len(day) > 2):
            return redirect("/mains/")

        # 날짜 정보
        year = int(date[0:4])
        month = int(date[4:])
        date_data = str(year) + " / " + str(month).zfill(2) +" / " + str(day).zfill(2)
        formatted_date = datetime(year, month, 1).strftime('%B %Y')

        try:
            # stella변수. 코드에서 이름으로 변환
            stella_name = models.Stellas.objects.get(stella_name_code = stella)
        except:
            return redirect("/mains/")

        # 키리누키(클립) 데이터(갯수) 불러오기
        kirinuky_data = models.kirinuky.objects.filter(
                kirinuky_day__year=year, kirinuky_day__month=month, kirinuky_day__day=day, kirinuky_stella__icontains = stella_name
            ).count()
        
        #bangsong_day = list(models.Replay.objects.filter(stella = stella, replay_day__year=year, replay_day__month=month))
        try:
            #방송 데이터 가져오기(에러 발생시, 해당 날짜에는 방송을 하지 않거나, 다시보기가 올라오지 않음.)
            bangsong_data = models.Replay.objects.filter(
                stella = stella_name, replay_day__year=year, replay_day__month=month, replay_day__day=day
            ).get()
            contents = bangsong_data.replay_contents
        except:
            contents = "해당하는 날짜에 대한 데이터가 없습니다."

        # 결과 출력
        return render(request,"members.html",
                        {   'stella': stella,
                            'string_date' : formatted_date,
                            'stella_name' : stella_name,
                            'total_date_data' : date_data,
                            'contents' : contents,
                            'clips' : str(kirinuky_data) + "개",
                            'for_calander_date':[year,month,day],})
                            #'bangsong_day' : bangsong_day})
    
# 클립 및 다시보기 추가하는 사이트
def add_page(request,category):
    # 사이트 입장
    if request.method == "GET":
        form = None
        if category == "clip":
            form = forms.clip_regist_form()
        if category == "reply":
            form = forms.reply_regist_form()
        return render(request,"add.html",{'form' : form,'category':category})
   
    # 데이터 등록
    if request.method == "POST":
        if category == "clip":
            stellas = request.POST.getlist('stellas')
            stella_list = ", ".join(stellas)
            form = forms.clip_regist_form(request.POST)
            if form.is_valid():
                # 링크의 아이디값 추출
                url1 = form.cleaned_data['kirinuky_link']
                url2 = url1.split('?v=')
                url3 = url2[1].split('&')
                url4 = "www.youtube.com/embed/" + url3

                clip_instance = form.save(commit=False)
                clip_instance.kirinuky_stella = stella_list
                clip_instance.kirinuky_link = url4
                
                clip_instance.save()
                return redirect("/")
            
        if category == "reply":
            form = forms.reply_regist_form(request.POST)
            if form.is_valid():

                # 링크의 아이디값 추출
                url1 = form.cleaned_data['replay_link']
                url2 = url1.split('?v=')
                url3 = url2[1].split('&')
                url4 = "www.youtube.com/embed/" + url3

                reply_instance = form.save(commit=False)
                reply_instance.replay_link = url4
                reply_instance.save()
                return redirect("/")