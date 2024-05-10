from django.shortcuts import render,redirect
from datetime import datetime
from . import models,forms



# 메인 페이지1(스텔라 선택 전.)
def main_page(request):
    if request.method == "GET":
        # 현재 날짜 정보
        current_datetime = datetime.now()
        # 날짜 포멧팅
        formatted_date = current_datetime.strftime('%B %Y')
        # 선택한 날짜와 오시가 없기에 현재 날짜에 대한 정보를 반환
        return render(request,"page.html",{
            'string_date' : formatted_date,
            'for_calander_date' : [
                current_datetime.year,
                current_datetime.month,
                current_datetime.day
            ]})
    
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
        try:
            formatted_date = datetime(year, month, 1).strftime('%B %Y')
            stella_name = models.Stellas.objects.get(stella_name_code = stella)
        except:
            return redirect("/errorpage")
        
        bangsong_day = list(models.Replay.objects.filter(
            stella = stella_name, 
            replay_day__year = year, 
            replay_day__month = month).values_list('replay_day__day', flat=True))


        return render(request,"members.html",
                      { 'stella': stella,
                        'string_date' : formatted_date,
                        'stella_name' : stella_name,
                        'total_date_data' : "아직 날짜가 설정되지 않았습니다.",
                        'contents' : "아직 날짜가 설정되지 않았습니다.",
                        'clips' : "아직 날짜가 설정되지 않았습니다.",
                        'for_calander_date':[year,month,0],
                        'bangsong_day' : bangsong_day})
    
# 메인 페이지3(날짜 선택 / 캘린더에 방송 한 날짜 굵게 표시 + 정보창에 정보 띄우기)
def stella_detail_page(request,stella,date,day):
    if request.method == "GET":

        # 일자를 잘못 입력 한 경우.
        if(int(day) > 31 or int(day) < 1):
            request.session['error_message'] = '일자 입력이 잘못되었습니다.'
            return redirect("/mains/"+stella+"/"+date)

        # 날짜 정보
        year = int(date[0:4])
        month = int(date[4:])
        date_data = str(year) + " / " + str(month).zfill(2) +" / " + str(day).zfill(2)
        
        # 변수 초기화
        contents = ""

        try:
            formatted_date = datetime(year, month, 1).strftime('%B %Y')
            # stella변수. 코드에서 이름으로 변환
            stella_name = models.Stellas.objects.get(stella_name_code = stella)
        except:
            return redirect("/errorpage")

        # 키리누키(클립) 데이터(갯수) 불러오기
        kirinuky_data = models.kirinuky.objects.filter(
                kirinuky_day__year=year, 
                kirinuky_day__month=month, 
                kirinuky_day__day=day, 
                kirinuky_stella__icontains = stella_name
            ).count()
    
        bangsong_day = list(models.Replay.objects.filter(
            stella = stella_name, 
            replay_day__year = year, 
            replay_day__month = month).values_list('replay_day__day', flat=True))

        #방송 데이터 가져오기(에러 발생시, 해당 날짜에는 방송을 하지 않거나, 다시보기가 올라오지 않음.)
        bangsong_data_list = models.Replay.objects.filter(
            stella = stella_name, 
            replay_day__year = year, 
            replay_day__month = month, 
            replay_day__day = day
        )

        # 리스트에 결과가 있을 때 처리
        if bangsong_data_list.exists():
            datas = []
            for i in bangsong_data_list:
                datas.append(i.replay_contents)
            contents = ", ".join(datas)
        else:
            contents = "해당하는 날짜에 대한 데이터가 없습니다."

        # 결과 출력
        return render(request,"members.html",
                        {   'stella': stella,
                            'string_date' : formatted_date,
                            'stella_name' : stella_name,
                            'total_date_data' : date_data,
                            'contents' : contents,
                            'clips' : str(kirinuky_data) + "개",
                            'for_calander_date':[year,month,day],
                            'bangsong_day' : bangsong_day})
    

####################################################################################################################################################################################################################
####################################################################################################################################################################################################################
####################################################################################################################################################################################################################
    
# 다시보기 및 클립 보기
def vedios(request,stella,date,day):
    if request.method == "GET":
        try:
            # stella변수. 코드에서 이름으로 변환
            stella_name = models.Stellas.objects.get(stella_name_code = stella)
        except:
            return redirect("/errorpage")

        year = int(date[0:4])
        month = int(date[4:])
        date_data = str(year) + " / " + str(month).zfill(2) +" / " + str(day).zfill(2)

        reply_date = models.Replay.objects.filter(
            stella=stella_name, 
            replay_day__year=year, 
            replay_day__month=month, 
            replay_day__day=day)
    
        kirinuky_data = models.kirinuky.objects.filter(
            kirinuky_day__year=year, 
            kirinuky_day__month=month, 
            kirinuky_day__day=day, 
            kirinuky_stella__icontains = stella_name)
        
        if(not(reply_date.exists() or kirinuky_data.exists())):
            request.session['error_message'] = '해당하는 날짜에 다시보기 혹은 클립이 하나도 등록되지 않습니다.'
            return redirect("/mains/"+stella+"/"+date+"/"+day)

        return render(request,"view.html",{
            'stella': stella_name,
            'total_date_data' : date_data,
            'reply_date' : reply_date,
            'kirinuky_data' : kirinuky_data,
        })

####################################################################################################################################################################################################################
####################################################################################################################################################################################################################
####################################################################################################################################################################################################################

# 링크 양식 구분 및 영상 아이디값 추출를 위한 함수
def get_link(url):
    url1 = url
    url4= ""
    pattern1 = "www.youtube.com/"
    pattern2 = "youtu.be/"           
    if pattern1 in url1:
        url2 = url1.split('?v=')
        url3 = url2[1].split('&')
        url4 = "www.youtube.com/embed/" + url3[0]
    elif pattern2 in url1:
        url2 = url1.split('youtu.be/')
        url3 = url2[1].split('?')
        url4 = "www.youtube.com/embed/" + url3[0]
    return url4


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
                url = get_link(form.cleaned_data['kirinuky_link'])
                clip_instance = form.save(commit=False)
                clip_instance.kirinuky_stella = stella_list
                clip_instance.kirinuky_link = url
                clip_instance.save()
                return redirect("/")
            
        if category == "reply":
            form = forms.reply_regist_form(request.POST)
            if form.is_valid():
                url = get_link(form.cleaned_data['replay_link'])
                reply_instance = form.save(commit=False)
                reply_instance.replay_link = url
                reply_instance.save()
                return redirect("/")
            
####################################################################################################################################################################################################################
####################################################################################################################################################################################################################
####################################################################################################################################################################################################################

def requests(request):
    if request.method == "GET":
        form = forms.requests_form()
        return render(request,"requests.html",{'form':form})

    if request.method == "POST":
        form = forms.requests_form(request.POST)
        category = request.POST.get('category')
        data_model = form.save(commit=False)
        data_model.requests_category = category
        data_model.save()
        return redirect("/")
    


####################################################################################################################################################################################################################
####################################################################################################################################################################################################################
####################################################################################################################################################################################################################


# 에러 발생시 처리
def custom_page_not_found_view(request, exception):
    return redirect("/errorpage")

def custom_error_view(request):
    return redirect("/errorpage")

def error_page(request):
    return render(request, "error.html", {})