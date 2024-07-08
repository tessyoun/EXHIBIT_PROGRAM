from django.db import models
from django.contrib.auth.models import User

class Reservation_hall(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hall_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    contact_position = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    event_scale = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.hall_name} - {self.company}"
