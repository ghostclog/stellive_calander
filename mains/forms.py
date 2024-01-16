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
