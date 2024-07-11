from django.db import models

#채팅 기록 저장

class ChatHistory(models.Model):
    question = models.TextField()
    answer = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Q: {self.question} | A: {self.answer}"


# 에이블스쿨 faq db.sqlite3
class faq_aivle(models.Model):
    qapk = models.TextField(db_column='qapk', primary_key=True,null=False)
    qacust = models.TextField(db_column='qacust', blank=True, null=False)
    qacat = models.TextField(db_column='qacat', blank=True, null=False) 
    qalist = models.TextField(db_column='qalist', blank=True, null=False)
    source = models.TextField(db_column='source', blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'chat_faq_aivle'
        
# 전시회 faq db.sqlite3
class faq_exhi(models.Model):
    qapk = models.TextField(db_column='qapk', primary_key=True,null=False)
    qacust = models.TextField(db_column='qacust', blank=True, null=False)
    qacat = models.TextField(db_column='qacat', blank=True, null=False) 
    qalist = models.TextField(db_column='qalist', blank=True, null=False)
    source = models.TextField(db_column='source', blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'chat_faq_exhi'

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
        
class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'