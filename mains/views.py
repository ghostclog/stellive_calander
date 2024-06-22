from django.shortcuts import render, redirect
from datetime import datetime
from . import models, forms

stella_dict={
    'kanna':'아이리 칸나',
    'yuni':'아야츠노 유니',
    'hina':'시라유키 히나',
    'shiro':'네네코 마시로',
    'lize':'아카네 리제',
    'tabi':'아라하시 타비',
    'shibuki':'텐코 시부키',
    'rin':'아오쿠모 린',
    'nana':'하나코 나나',
    'riko':'유즈하 리코'
}


# 메인 페이지 1 (스텔라 선택 전)
def main_page(request):
    """
    스텔라 선택 전 메인 페이지를 보여줍니다.
    현재 날짜 정보를 기반으로 렌더링합니다.

    Args:
        request (HttpRequest): HTTP 요청 객체
    """
    if request.method == "GET":
        current_datetime = datetime.now()  # 현재 날짜 및 시간
        formatted_date = current_datetime.strftime('%B %Y')  # 월(영문) 연도 형식으로 포맷
        return render(request, "page.html", {
            'string_date': formatted_date,
            'for_calander_date': [
                current_datetime.year,
                current_datetime.month,
                current_datetime.day
            ]})

# 메인 페이지 2 (스텔라 선택 후, 최신 연월 캘린더)
def stella_default_page(request, stella):
    """
    스텔라 선택 후 기본 메인 페이지로 리디렉션합니다.
    최신 연월을 기준으로 캘린더 페이지로 이동합니다.

    Args:
        request (HttpRequest): HTTP 요청 객체
        stella (str): 선택된 스텔라 이름 코드
    """
    if request.method == "GET":
        year = str(datetime.now().year)
        month = str(datetime.now().month)
        redirect_url = f"/mains/{stella}/{year}{month.zfill(2)}"  # 최신 연월 캘린더 페이지 URL
        return redirect(redirect_url)

# 메인 페이지 3 (스텔라 및 연월 선택, 캘린더)
def stella_date_page(request, stella, date):
    """
    특정 스텔라와 연월을 선택한 메인 페이지를 보여줍니다.
    해당 스텔라의 방송 날짜를 캘린더에 표시합니다.

    Args:
        request (HttpRequest): HTTP 요청 객체
        stella (str): 선택된 스텔라 이름 코드
        date (str): 선택된 연월 (YYYYMM 형식)
    """
    if request.method == "GET":
        year = int(date[0:4])
        month = int(date[4:])
        try:
            formatted_date = datetime(year, month, 1).strftime('%B %Y')  # 월(영문) 연도 형식
            stella_name = models.Stellas.objects.get(stella_name_code=stella)  # 스텔라 객체 조회
        except models.Stellas.DoesNotExist:  # 스텔라가 존재하지 않을 경우
            return redirect("/errorpage")

        bangsong_day = list(models.Replay.objects.filter(
            stella=stella_name,
            replay_day__year=year,
            replay_day__month=month
        ).values_list('replay_day__day', flat=True))  # 방송 날짜 목록

        kirinuky_day = list(models.kirinuky.objects.filter(
            kirinuky_stella__contains = stella_dict[stella],
            kirinuky_day__year=year,
            kirinuky_day__month=month
        ).values_list('kirinuky_day__day', flat=True))

        return render(request, "members.html", {
            'stella': stella,
            'string_date': formatted_date,
            'stella_name': stella_name,
            'total_date_data': "아직 날짜가 설정되지 않았습니다.",  # 상세 날짜 정보 (초기값)
            'contents': "아직 날짜가 설정되지 않았습니다.",        # 방송 내용 (초기값)
            'clips': "아직 날짜가 설정되지 않았습니다.",          # 클립 개수 (초기값)
            'for_calander_date': [year, month, 0],                  # 캘린더 표시 날짜
            'bangsong_day': bangsong_day,                           # 방송 날짜 목록
            'kirinuky_day' : kirinuky_day
        })

# 메인 페이지 4 (스텔라, 연월, 일자 선택, 상세 정보)
def stella_detail_page(request, stella, date, day):
    """
    특정 스텔라, 연월, 일자를 선택한 상세 페이지를 보여줍니다.
    해당 날짜의 방송 정보, 클립 개수 등을 표시합니다.

    Args:
        request (HttpRequest): HTTP 요청 객체
        stella (str): 선택된 스텔라 이름 코드
        date (str): 선택된 연월 (YYYYMM 형식)
        day (int): 선택된 일자
    """

    if request.method == "GET":
        # 스텔라 정보가 없는 경우
        if(stella == "not_select"):
            return redirect("/")
        

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
        
        kirinuky_day = list(models.kirinuky.objects.filter(
            kirinuky_stella__contains = stella_dict[stella],
            kirinuky_day__year=year,
            kirinuky_day__month=month
        ).values_list('kirinuky_day__day', flat=True))

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
            contents = " / ".join(datas)
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
                            'bangsong_day' : bangsong_day,
                            'kirinuky_day' : kirinuky_day})
    
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

# 링크 양식 구분 및 영상 아이디값 추출를 위한 함수
# 유튜브 링크에서 임베드 링크 추출
def get_link(url, category):  
    """
    유튜브 링크(url)를 받아 임베드 링크를 반환합니다.
    데이터베이스에 이미 존재하는 링크인 경우 None을 반환합니다.

    Args:
        url (str): 유튜브 링크 (일반 또는 단축 링크)
        category (str): 링크 종류 ("clip" 또는 "reply")

    Returns:
        str or None: 임베드 링크 또는 None (이미 존재하는 경우)
    """

    url1 = url  # 원본 URL 저장
    url4 = ""  # 추출할 임베드 URL 초기화
    pattern1 = "www.youtube.com/"  # 일반 유튜브 링크 패턴
    pattern2 = "youtu.be/"       # 단축 유튜브 링크 패턴

    if pattern1 in url1:  # 일반 유튜브 링크 처리
        url2 = url1.split('?v=')
        url3 = url2[1].split('&')
        url4 = "www.youtube.com/embed/" + url3[0]
    elif pattern2 in url1:  # 단축 유튜브 링크 처리
        url2 = url1.split('youtu.be/')
        url3 = url2[1].split('?si=')
        url4 = "www.youtube.com/embed/" + url3[0]
    else:
        return None

    # 데이터베이스 조회 (중복 링크 확인)
    if category == "clip":
        exists = models.kirinuky.objects.filter(kirinuky_link=url4).exists()
    elif category == "reply":
        exists = models.Replay.objects.filter(replay_link=url4).exists()

    if exists:  # 이미 존재하는 링크인 경우
        return None  
    else:  # 새로운 링크인 경우
        return url4


# 클립 및 다시보기 추가 페이지 처리
def add_page(request, category):
    """
    클립 또는 다시보기 추가 페이지를 처리하는 뷰 함수입니다.

    Args:
        request (HttpRequest): HTTP 요청 객체
        category (str): 페이지 종류 ("clip" 또는 "reply")
    """

    # GET 요청: 페이지 표시
    if request.method == "GET":
        form = None
        if category == "clip":
            form = forms.clip_regist_form()
        if category == "reply":
            form = forms.reply_regist_form()
        return render(request, "add.html", {'form': form, 'category': category})

    # POST 요청: 데이터 등록
    if request.method == "POST":

        if category == "clip":
            stellas = request.POST.getlist('stellas')
            stella_list = ", ".join(stellas)
            form = forms.clip_regist_form(request.POST)
            if form.is_valid():
                url = get_link(form.cleaned_data['kirinuky_link'], category)  # 링크 추출 및 중복 확인
                if url is None:  # 이미 존재하는 링크 처리
                    return redirect("/")
                
                clip_instance = form.save(commit=False)
                clip_instance.kirinuky_stella = stella_list
                clip_instance.kirinuky_link = url
                clip_instance.save()
                return redirect("/")

        if category == "reply":
            form = forms.reply_regist_form(request.POST)
            if form.is_valid():
                url = get_link(form.cleaned_data['replay_link'], category)  # 링크 추출 및 중복 확인
                if url is None:  # 이미 존재하는 링크 처리
                    return redirect("/")
                
                reply_instance = form.save(commit=False)
                reply_instance.replay_link = url
                reply_instance.save()
                return redirect("/")
            
####################################################################################################################################################################################################################

# 사용자 요청사항 처리
def requests(request):
    """
    사용자 요청사항 페이지를 처리하는 뷰 함수입니다.

    GET 요청: 요청사항 입력 폼을 보여줍니다.
    POST 요청: 제출된 요청사항을 데이터베이스에 저장하고 메인 페이지로 리디렉션합니다.

    Args:
        request (HttpRequest): HTTP 요청 객체
    """
    if request.method == "GET":  # GET 요청 처리
        form = forms.requests_form()  # 요청사항 입력 폼 생성
        return render(request, "requests.html", {'form': form})  # 폼을 포함하여 페이지 렌더링

    if request.method == "POST":  # POST 요청 처리 (요청사항 제출)
        form = forms.requests_form(request.POST)  # 제출된 데이터로 폼 객체 생성
        if form.is_valid():  # 유효성 검사
            category = request.POST.get('category')  # 요청 유형 (카테고리) 가져오기
            data_model = form.save(commit=False)  # 모델 객체 생성 (아직 저장하지 않음)
            data_model.requests_category = category  # 요청 유형 설정
            data_model.save()  # 데이터베이스에 저장
            return redirect("/")
        else:
            # 유효성 검사 실패 시 처리 (오류 메시지 표시 등)
            return render(request, "requests.html", {'form': form}) 

####################################################################################################################################################################################################################

# 에러 발생시 처리
def custom_page_not_found_view(request, exception):
    return redirect("/errorpage")

def custom_error_view(request):
    return redirect("/errorpage")

def error_page(request):
    return render(request, "error.html", {})