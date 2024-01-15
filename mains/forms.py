from django import forms
from . import models

class reply_regist_form(forms.Form):
    class Meta:
        model = models.Replay
        fields = [
            'stella',
            'replay_link', 
            'replay_day', 
            'replay_contents']
    

class clip_regist_form(forms.Form):
    model = models.Replay
    fields = [
        'kirinuky_stella', 
        'kirinuky_link', 
        'kirinuky_title', 
        'kirinuky_day']
