# Generated by Django 4.0.4 on 2022-05-14 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0012_file_downloadmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file_downloadmodel',
            old_name='file_uploded_date',
            new_name='file_download_date',
        ),
    ]