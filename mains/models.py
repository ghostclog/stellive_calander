from django.db import models

# Create your models here.

class Stellas(models.Model):    # 있으면 편할거 같아서 추가함
    stella_name = models.CharField(primary_key=True,max_length=30)

    def __str__(self):  # 스텔라 이름 반환
        return self.stel_name

class Replay(models.Model):
    stellas =  models.CharField(max_length=300)
    replay_link = models.CharField(max_length=300)      # 다시보기 링크
    replay_day = models.DateField()             #다시보기 날짜
    replay_contents = models.CharField(max_length=100)  #다시보기 내용

class kirinuky(models.Model):
    kirinuky_stella = models.CharField(max_length=30)   # 외래키
    kirinuky_link = models.CharField(max_length=300)    # 클립 링크
    kirinuky_title = models.CharField(max_length=50)    # 클립명
    replay_id = models.ForeignKey(Replay, on_delete=models.CASCADE)    # 외래키