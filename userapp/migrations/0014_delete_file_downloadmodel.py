# Generated by Django 4.0.4 on 2022-05-14 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0013_rename_file_uploded_date_file_downloadmodel_file_download_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='file_downloadModel',
        ),
    ]
