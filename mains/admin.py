from django.contrib import admin
from .models import kirinuky,Replay, Stellas

class KirinukyAdmin(admin.ModelAdmin):
    search_fields = ['kirinuky_title', 'kirinuky_stella']  # 검색할 필드 지정

class ReplayAdmin(admin.ModelAdmin):
    search_fields = ['replay_contents']  # Replay 모델의 검색 필드
    list_filter = ['stella__stella_name']# 스텔라별 필터링 추가

admin.site.register(kirinuky, KirinukyAdmin)
admin.site.register(Replay, ReplayAdmin)
admin.site.register(Stellas)  # Stellas 모델도 등록해야 필터링 가능