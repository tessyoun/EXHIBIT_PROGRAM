from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):
    USER_TYPE_CHOICES = (
        (None, '선택'),
        ('일반회원', '일반회원'),
        ('기업회원', '기업회원'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='선택')
    name = models.CharField(max_length=100, null=True, blank=True, default='regular')
    phone_number = models.CharField(max_length=20)
    