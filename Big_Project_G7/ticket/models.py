from django.db import models

class TicketBoughtInfo(models.Model):
    userticketid = models.AutoField(db_column='UserTicketID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(blank=True, null=True)
    exhibitionid = models.IntegerField(db_column='ExhibitionID', blank=True, null=True)  # Field name made lowercase.
    ticketid = models.IntegerField(db_column='TicketID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ticket_bought_info'
