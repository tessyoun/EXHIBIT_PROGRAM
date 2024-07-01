# Generated by Django 5.0.6 on 2024-07-01 01:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_alter_profile_name_alter_profile_user_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="booth_date_edit",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="booth_name_edit",
            field=models.CharField(default="boothname", max_length=20),
        ),
        migrations.AddField(
            model_name="profile",
            name="booth_pic_edit",
            field=models.ImageField(
                blank=True, null=True, upload_to="profile_pictures/"
            ),
        ),
    ]
