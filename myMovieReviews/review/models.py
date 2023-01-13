from django.db import models
from django.urls import reverse

# Create your models here.
class review(models.Model):
    title = models.CharField(max_length=100, null=True)
    year = models.CharField(max_length=100, null=True)
    genre = models.CharField(max_length=100, null=True)
    star = models.CharField(max_length=100, null=True)
    runningtime = models.CharField(max_length=100, null=True)
    reviewtext = models.CharField(max_length=100, null=True)
    director = models.CharField(max_length=100, null=True)
    actor = models.CharField(max_length=100, null=True)
    url = models.URLField('Site URL')

    def __str__(self):
        return "제목 : "+self.title+", 개봉년도 : "+self.year+", 장르 : "+self.year+", 별점 : "+self.star+", 러닝타임 : "+self.runningtime+", 리뷰 : "+self.reviewtext+", 감독 : "+self.director+", 배우 : "+self.director+" "
    def get_absolute_url(self):
        return reverse('detail', args=[(self.id)])
