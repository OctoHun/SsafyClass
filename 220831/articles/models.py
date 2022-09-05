from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10) # 필수 키워드 인자 max_length 최대 255
    content = models.TextField() # 글자 수 많을 때(최대길이 각각 다름)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)