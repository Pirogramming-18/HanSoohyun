from django.contrib import admin

# Register your models here.
# 내가 만든 모델을 관리자 페이지에서 관리할수있게 등록
from .models import review

admin.site.register(review)