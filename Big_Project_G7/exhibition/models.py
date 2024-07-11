# exhibition/models.py
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

# 전시회 홍보 이미지 업로드
class ImageUpload(models.Model):
    title = models.CharField(max_length=50, null=False)
    image = models.ImageField(upload_to='exhibition/',blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return f'{self.title}'
    
class Exhibition(models.Model):
    HALL_TYPE_CHOICES = (
        ('', '선택'),
        ('A홀', 'A홀'),
        ('B홀', 'B홀'),
        ('C홀', 'C홀')
    )
    exhibition_name = models.CharField(primary_key=True, max_length=50)
    host_id = models.CharField(max_length=50)
    hall = models.CharField(choices=HALL_TYPE_CHOICES, default='', max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_booths = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.exhibition_name}'
    
    class Meta:
        managed = False
        db_table = 'exhibition_exhibition'

class Exhibition_info(models.Model):
    HALL_TYPE_CHOICES = (
        ('', '선택'),
        ('1', 'A홀'),
        ('2', 'B홀'),
        ('3', 'C홀'),
        ('4', 'D홀'),
    )
    exhibition_id = models.AutoField(primary_key=True, db_column='ExhibitionID')
    exhibition_name = models.CharField(max_length=100, db_column='ExhibitionName')
    exhibition_description = models.CharField(max_length=100, db_column='ExhibitionDescription')
    start_date = models.DateField(db_column='ExhibitionRegistrationDate')
    host_id = models.IntegerField(db_column='OrganizationID', unique=True)
    hall_id = models.CharField(choices=HALL_TYPE_CHOICES, default='',db_column='Hall_ID', max_length=50)
    end_date = models.DateField(db_column='ExhibitionClosedDate')
    
    class Meta:
        managed = False
        db_table = 'Exhibition_info'
        
    def __str__(self):
        return f'{self.exhibition_name}'
    