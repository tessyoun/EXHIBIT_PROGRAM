from django.db import models
from django.contrib.auth.models import User

class Program(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='programs')
    name = models.CharField(max_length=100)
    description = models.TextField()
    company_name = models.CharField(max_length=100)
    selected_times = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class BoothProgramReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    num_of_people = models.IntegerField()
    reservationtime = models.CharField(max_length=45)

    def __str__(self):
        return self.user_name
