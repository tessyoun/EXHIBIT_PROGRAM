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