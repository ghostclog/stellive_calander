from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),  # 메인 페이지1(스텔라 선택 전.)
    path('mains/<str:stella>', views.stella_default_page),  # 메인 페이지2(스텔라 선택 후.)
    path('mains/<str:stella>/<str:date>', views.stella_date_page),  # 메인 페이지3(스텔라 선택. 연월 선택)
    path('mains/<str:stella>/<str:date>/<str:day>', views.stella_detail_page),  # 메인 페이지3(날짜 선택)
    path('mains/<str:stella>/<str:date>/<str:day>/show', views.vedios),  # 날짜 자세히 보기

    path('add/<str:category>', views.add_page,name='add'),  # 키리누키 및 다시보기 정보 추가
    path('requests', views.requests),  # 요청사항
    path('feedback', views.stella_detail_page),  # 피드백
    
    path('errorpage', views.error_page),  # 에러페이지
]

handler404 = 'mains.views.custom_page_not_found_view'
handler500 = 'mains.views.custom_error_view'
