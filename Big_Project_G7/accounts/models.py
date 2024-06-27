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
    

# class UserProfile(models.Model):
#     USER_TYPE_CHOICES = (
#         ('regular', '일반회원'),
#         ('business', '기업회원'),
#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
#     name = models.CharField(max_length=100, null=True, blank=True)
#     company_name = models.CharField(max_length=100, null=True, blank=True)
#     phone = models.CharField(max_length=50)

#     def __str__(self):
#         return self.user.username