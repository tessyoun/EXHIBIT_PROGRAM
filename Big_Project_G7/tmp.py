# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountsProfile(models.Model):
    user_type = models.CharField(max_length=30)
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=19)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_profile'


class AuthGroup(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthPermission(models.Model):
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    permission_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class BoothBookmark(models.Model):
    boothbookmarkid = models.AutoField(db_column='BoothBookmarkID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(blank=True, null=True)
    boothid = models.IntegerField(db_column='BoothID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'booth_bookmark'


class BoothInfo(models.Model):
    boothid = models.AutoField(db_column='BoothID', primary_key=True)  # Field name made lowercase.
    boothname = models.CharField(db_column='BoothName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    companyid = models.IntegerField(db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    exhibitionid = models.IntegerField(db_column='ExhibitionID', blank=True, null=True)  # Field name made lowercase.
    exhibitioncategory = models.CharField(db_column='ExhibitionCategory', max_length=100, blank=True, null=True)  # Field name made lowercase.
    boothdescription1 = models.TextField(db_column='BoothDescription1', blank=True, null=True)  # Field name made lowercase.
    boothdescription2 = models.TextField(db_column='BoothDescription2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'booth_info'


class ChatFaqAivle(models.Model):
    qapk = models.TextField(blank=True, null=True)
    qacust = models.TextField(blank=True, null=True)
    qacat = models.TextField(blank=True, null=True)
    qalist = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_faq_aivle'


class ChatFaqExhi(models.Model):
    qapk = models.TextField(blank=True, null=True)
    qacust = models.TextField(blank=True, null=True)
    qacat = models.TextField(blank=True, null=True)
    qalist = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_faq_exhi'


class ChatgptChathistory(models.Model):
    question = models.TextField()
    answer = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'chatgpt_chathistory'


class Chathistory(models.Model):
    chatid = models.AutoField(db_column='ChatID', primary_key=True)  # Field name made lowercase.
    chattimestamp = models.DateTimeField(db_column='ChatTimestamp')  # Field name made lowercase.
    inquiry = models.TextField(db_column='Inquiry', blank=True, null=True)  # Field name made lowercase.
    response = models.TextField(db_column='Response', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chathistory'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    action_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=62)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ExhibitionExhibition(models.Model):
    exhibition_name = models.CharField(primary_key=True, max_length=50)
    host_id = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_booths = models.IntegerField()
    hall = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'exhibition_exhibition'


class ExhibitionHall(models.Model):
    exhibitionhallid = models.AutoField(db_column='ExhibitionHallID', primary_key=True)  # Field name made lowercase.
    halldescription = models.TextField(db_column='HallDescription', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exhibition_hall'


class ExhibitionImageupload(models.Model):
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'exhibition_imageupload'


class ExhibitionInfo(models.Model):
    exhibitionid = models.AutoField(db_column='ExhibitionID', primary_key=True)  # Field name made lowercase.
    exhibitionname = models.CharField(db_column='ExhibitionName', max_length=100)  # Field name made lowercase.
    exhibitiondescription = models.TextField(db_column='ExhibitionDescription', blank=True, null=True)  # Field name made lowercase.
    exhibitionregistrationdate = models.DateField(db_column='ExhibitionRegistrationDate', blank=True, null=True)  # Field name made lowercase.
    organizationid = models.IntegerField(db_column='OrganizationID', blank=True, null=True)  # Field name made lowercase.
    hall_id = models.IntegerField(db_column='Hall_ID', blank=True, null=True)  # Field name made lowercase.
    exhibitioncloseddate = models.DateField(db_column='ExhibitionClosedDate', blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exhibition_info'


class ExhibitionNotice(models.Model):
    noticeid = models.AutoField(db_column='NoticeID', primary_key=True)  # Field name made lowercase.
    authorname = models.CharField(db_column='AuthorName', max_length=100)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=200)  # Field name made lowercase.
    content = models.TextField(db_column='Content')  # Field name made lowercase.
    reason = models.TextField(db_column='Reason', blank=True, null=True)  # Field name made lowercase.
    registrationdate = models.DateTimeField(db_column='RegistrationDate', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exhibition_notice'


class ExhibitionTicketInfo(models.Model):
    ticketid = models.AutoField(db_column='TicketID', primary_key=True)  # Field name made lowercase.
    exhibitionid = models.IntegerField(db_column='ExhibitionID')  # Field name made lowercase.
    audience = models.CharField(db_column='Audience', max_length=5)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exhibition_ticket_info'


class NoticeNotice(models.Model):
    update_time = models.DateTimeField()
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_time = models.DateTimeField()
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'notice_notice'


class ProgramInfo(models.Model):
    programid = models.AutoField(db_column='ProgramID', primary_key=True)  # Field name made lowercase.
    programname = models.CharField(db_column='ProgramName', max_length=200)  # Field name made lowercase.
    programdescription = models.TextField(db_column='ProgramDescription')  # Field name made lowercase.
    boothid = models.IntegerField(db_column='BoothID', blank=True, null=True)  # Field name made lowercase.
    boothname = models.CharField(db_column='BoothName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    companyid = models.IntegerField(db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'program_info'


class ProgramReservHistory(models.Model):
    reservationid = models.AutoField(db_column='ReservationID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(blank=True, null=True)
    programtimeid = models.IntegerField(db_column='ProgramTimeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'program_reserv_history'


class ProgramTime(models.Model):
    programtimeid = models.AutoField(db_column='ProgramTimeID', primary_key=True)  # Field name made lowercase.
    programid = models.IntegerField(db_column='ProgramID')  # Field name made lowercase.
    programtime = models.DateTimeField(db_column='ProgramTime')  # Field name made lowercase.
    programseats = models.IntegerField(db_column='ProgramSeats')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'program_time'


class ReserveHallReservationHall(models.Model):
    id = models.BigAutoField(primary_key=True)
    hall_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    contact_position = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=254)
    event_scale = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'reserve_hall_reservation_hall'


class SqliteSequence(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sqlite_sequence'


class TicketBoughtInfo(models.Model):
    userticketid = models.AutoField(db_column='UserTicketID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(blank=True, null=True)
    exhibitionid = models.IntegerField(db_column='ExhibitionID', blank=True, null=True)  # Field name made lowercase.
    ticketid = models.IntegerField(db_column='TicketID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ticket_bought_info'
