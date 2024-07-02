from django.db import models

# 부스 1 db.sqlite3
class exbooth_1st(models.Model):
    group = models.TextField(db_column='group', primary_key=True,null=False)
    bname = models.TextField(db_column='bname', blank=True, null=False)
    bcat = models.TextField(db_column='bcat', blank=True, null=False) 
    background = models.TextField(db_column='background', blank=True, null=True)
    service = models.TextField(db_column='service', blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'exbooth_1st'
        
# 부스 2 db.sqlite3
class exbooth_2nd(models.Model):
    group = models.TextField(db_column='group', primary_key=True,null=False)
    bname = models.TextField(db_column='bname', blank=True, null=False)
    bcat = models.TextField(db_column='bcat', blank=True, null=False) 
    background = models.TextField(db_column='background', blank=True, null=True)
    service = models.TextField(db_column='service', blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'exbooth_2nd'
        
# 부스 3 db.sqlite3
class exbooth_3rd(models.Model):
    group = models.TextField(db_column='group', primary_key=True,null=False)
    bname = models.TextField(db_column='bname', blank=True, null=False)
    bcat = models.TextField(db_column='bcat', blank=True, null=False) 
    background = models.TextField(db_column='background', blank=True, null=True)
    service = models.TextField(db_column='service', blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'exbooth_3rd'

# 부스 4 db.sqlite3
class exbooth_4th(models.Model):
    group = models.TextField(db_column='group', primary_key=True,null=False)
    bname = models.TextField(db_column='bname', blank=True, null=False)
    bcat = models.TextField(db_column='bcat', blank=True, null=False) 
    background = models.TextField(db_column='background', blank=True, null=True)
    service = models.TextField(db_column='service', blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'exbooth_4th'

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