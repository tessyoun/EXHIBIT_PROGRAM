from django.db import models

class TicketBoughtInfo(models.Model):
    userticketid = models.AutoField(db_column='UserTicketID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField()
    exhibitionid = models.IntegerField(db_column='ExhibitionID')  # Field name made lowercase.
    ticketid = models.CharField(db_column='TicketID', max_length=100, unique=True)  # Field name made lowercase.
    adult = models.IntegerField(db_column='adult')
    child = models.IntegerField(db_column='child')
    reservationDate = models.DateField(db_column='reservationDate')
    
    class Meta:
        managed = False
        db_table = 'ticket_bought_info'
