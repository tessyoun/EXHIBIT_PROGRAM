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