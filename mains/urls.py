from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),  # 메인 페이지
    path('<str:stella>', views.stella_page),  # 메인 페이지

]