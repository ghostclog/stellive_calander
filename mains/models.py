from django.db import models

# Create your models here.

class Stellas(models.Model):    # 있으면 편할거 같아서 추가함
    stella_name = models.CharField(primary_key=True,max_length=30)
    stella_name_code = models.CharField(max_length=30,null=True)
    for_order = models.IntegerField(default=0)  # 정렬 순서 필드 추가

    def __str__(self):  # 스텔라 이름 반환
        return self.stella_name
    
    class Meta:
        ordering = ['for_order']  # for_order 필드를 기준으로 정렬

class Replay(models.Model):
    stella =  models.ForeignKey(Stellas, on_delete=models.CASCADE)  # 스텔라
    replay_link = models.CharField(max_length=300)                  # 다시보기 링크
    replay_day = models.DateField()                                 # 다시보기 날짜
    replay_contents = models.CharField(max_length=100)              # 다시보기 내용

    def __str__(self):  # 관리자 페이지용
        return f"{self.stella} : {self.replay_day} - {self.replay_contents}"

class kirinuky(models.Model):
    kirinuky_stella = models.CharField(max_length=30)   # 스텔라들. string 형태
    kirinuky_link = models.CharField(max_length=300)    # 클립 링크
    kirinuky_title = models.CharField(max_length=50)    # 클립명
    kirinuky_day = models.DateField(null=True)          # 클립 원본 날짜

    def __str__(self):  # 관리자 페이지용
        return self.kirinuky_title

class requests(models.Model):
    requests_category = models.CharField(max_length=20)
    requests_con = models.CharField(max_length=200)