from django.db import models
from django.contrib.auth.models import User

class Program(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    company_name = models.CharField(max_length=100)
    selected_times = models.CharField(max_length=255)  # 이 줄을 추가합니다

    def __str__(self):
        return self.name
