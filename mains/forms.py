from django import forms
from . import models

class reply_regist_form(forms.ModelForm):
    class Meta:
        model = models.Replay
        fields = [
            'stella',
            'replay_link', 
            'replay_day', 
            'replay_contents']
        widgets = {
            'replay_day': forms.DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super(reply_regist_form, self).__init__(*args, **kwargs)
        # 각 필드의 위젯을 Textarea로 변경
        self.fields['replay_contents'].widget = forms.Textarea(attrs={'rows': 5, 'cols': 40,
                                                                      'placeholder': '저스트 챗팅 / 노래방 / 카페 탐방'})

class clip_regist_form(forms.ModelForm):
    class Meta:
        model = models.kirinuky

        fields = [
            'kirinuky_link', 
            'kirinuky_title', 
            'kirinuky_day']
        
        widgets = {
            'kirinuky_day': forms.DateInput(attrs={'type': 'date'}),
        }

        labels = {
            'kirinuky_link':'키리누키(클립) 링크',
            'kirinuky_title':'키리누키(클립) 제목',
            'kirinuky_day':'방송 일자',
        }

    def __init__(self, *args, **kwargs):
        super(clip_regist_form, self).__init__(*args, **kwargs)
        # 각 필드의 위젯을 Textarea로 변경
        self.fields['kirinuky_title'].widget = forms.Textarea(attrs={'rows': 5, 'cols': 40,
                                                                     'placeholder': '제목 그대로 복붙하시면 됩니다.'}) 
        
class requests_form(forms.ModelForm):
    class Meta:
        model = models.requests

        fields = [
            'requests_con']
        labels = {
            'requests_con': '요청 내용'
        }
    
    def __init__(self, *args, **kwargs):
        super(requests_form, self).__init__(*args, **kwargs)
        # 각 필드의 위젯을 Textarea로 변경
        self.fields['requests_con'].widget = forms.Textarea(attrs={'rows': 5, 'cols': 40,
                                                                     'placeholder': '0. 사이트 자체에 대한 요청사항은 피드백 탭에서 요청해주세요! \n1. 잘못된 날짜와 스텔라를 알려주세요. \n2. 키리누키의 경우 제목도 같이 올려주세요!'})