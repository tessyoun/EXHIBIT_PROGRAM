from django.db import models
from django.contrib.auth.models import User

class Booth(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    company_name = models.CharField(max_length=100, default='default_company')  # 기본 값 추가

    def __str__(self):
        return self.name  # 객체를 프로그램명으로 표현

class Program(models.Model):
    booth = models.ForeignKey(Booth, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name  # 객체를 프로그램명으로 표현

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    reserved_time = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.program.name} at {self.reserved_time}"  # 예약 객체를 프로그램명과 시간으로 표현
