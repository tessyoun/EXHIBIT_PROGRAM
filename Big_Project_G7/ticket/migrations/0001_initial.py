# Generated by Django 5.0.6 on 2024-07-11 04:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TicketBoughtInfo",
            fields=[
                (
                    "userticketid",
                    models.AutoField(
                        db_column="UserTicketID", primary_key=True, serialize=False
                    ),
                ),
                ("user_id", models.IntegerField(blank=True, null=True)),
                (
                    "exhibitionid",
                    models.IntegerField(
                        blank=True, db_column="ExhibitionID", null=True
                    ),
                ),
                (
                    "ticketid",
                    models.IntegerField(blank=True, db_column="TicketID", null=True),
                ),
            ],
            options={
                "db_table": "ticket_bought_info",
                "managed": False,
            },
        ),
    ]
