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
        app_label = 'mysite'
        
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
        app_label = 'mysite'
        
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
        app_label = 'mysite'

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
        app_label = 'mysite'