# Generated by Django 4.0.4 on 2022-05-13 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_usermodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='otp',
            field=models.IntegerField(null=True),
        ),
    ]
