from django.db import models

class TicketBoughtInfo(models.Model):
    userticketid = models.AutoField(db_column='UserTicketID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField()
    exhibitionid = models.IntegerField(db_column='ExhibitionID')  # Field name made lowercase.
    ticketid = models.IntegerField(db_column='TicketID', unique=True)  # Field name made lowercase.
    adult = models.IntegerField(db_column='adult')
    child = models.IntegerField(db_column='child')
    
    class Meta:
        managed = False
        db_table = 'ticket_bought_info'
