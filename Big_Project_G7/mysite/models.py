from django.db import models

# 전시회 부스 데이터 db.sqlite3
class Booth_Info(models.Model):
    booth_id = models.IntegerField(db_column='BoothID', primary_key=True, null=False)
    booth_name = models.TextField(db_column='BoothName', blank=True, null=True)
    company_id = models.IntegerField(db_column='CompanyID', blank=True, null=True)
    company_name = models.TextField(db_column='CompanyName', blank=True, null=True)
    exhibition_id = models.IntegerField(db_column='ExhibitionID', blank=True, null=True)
    booth_category = models.TextField(db_column='ExhibitionCategory', blank=True, null=True)
    background = models.TextField(db_column='BoothDescription1', blank=True, null=True)
    service = models.TextField(db_column='BoothDescription2', blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'Booth_Info'
        app_label ='mysite'

# class Bookmarks(models.Model):
#     user_id = models.IntegerField(db_column='user_id', primary_key=True, null=False)
#     booth_id = models.IntegerField(db_column='BoothID', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'booth_bookmark'
#         app_label ='mysite'