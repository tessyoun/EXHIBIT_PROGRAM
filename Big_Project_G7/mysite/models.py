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
#     bookmark = models.TextField(db_column='BoothBookmarkID', blank=True, null=False)
#     user_id = models.IntegerField(db_column='user_id', primary_key=True, null=True)
#     booth_id = models.IntegerField(db_column='BoothID', blank=True, null=True)
    
#     class Meta:
#         managed = False
#         db_table = 'Bookmarks'
#         app_label ='mysite'

#전시회 홀 정보
class ExhibitionHall(models.Model):
    ExhibitionHallID = models.AutoField(primary_key=True, db_column='ExhibitionHallID')
    ExhibitionHallDescription = models.CharField(max_length=255, db_column='HallDescription')

    def __str__(self):
        return self.ExhibitionHallDescription

    class Meta:
        managed = False
        db_table = 'exhibition_hall'
        app_label ='mysite'

# 전시회 정보
class ExhibitionInfo(models.Model):
    ExhibitionID = models.AutoField(primary_key=True, db_column='ExhibitionID')
    ExhibitionName = models.CharField(max_length=255, db_column='ExhibitionName')
    ExhibitionDescription = models.TextField(blank=True, null=True, db_column='ExhibitionDescription')
    ExhibitionRegistrationDate = models.DateField(blank=True, null=True, db_column='ExhibitionRegistrationDate')
    OrganizationID = models.FloatField(blank=True, null=True, db_column='OrganizationID')
    Hall_ID = models.ForeignKey(ExhibitionHall, on_delete=models.CASCADE, blank=True, null=True, db_column='Hall_ID')
    ExhibitionClosedDate = models.DateField(blank=True, null=True, db_column='ExhibitionClosedDate')
    ExhibitionURL = models.TextField(blank=True, null=True, db_column='URL')
    ExhibitionImageURL = models.TextField(max_length=255, blank=True, null=True, db_column='PosterImg') #포스터 이미지

    def __str__(self):
        return self.ExhibitionName

    class Meta:
        managed = False
        db_table = 'exhibition_info'
        app_label ='mysite'
