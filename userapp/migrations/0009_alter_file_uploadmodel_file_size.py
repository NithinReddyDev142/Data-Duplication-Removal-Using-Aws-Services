# Generated by Django 4.0.4 on 2022-05-13 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_alter_file_uploadmodel_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_uploadmodel',
            name='file_size',
            field=models.BigIntegerField(help_text='file_size', null=True),
        ),
    ]
