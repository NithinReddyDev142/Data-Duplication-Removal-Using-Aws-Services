# Generated by Django 4.0.4 on 2022-05-12 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='file_uploadModel',
            fields=[
                ('file_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('file', models.FileField(upload_to='user_image/')),
                ('file_name', models.CharField(help_text='file_name', max_length=200)),
                ('file_size', models.BigIntegerField(help_text='file_size', max_length=200)),
                ('file_type', models.CharField(help_text='file_type', max_length=300)),
                ('file_uploaded_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'file_details',
            },
        ),
        migrations.CreateModel(
            name='userModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(help_text='user_name', max_length=50)),
                ('email', models.CharField(help_text=' email', max_length=50)),
                ('password', models.CharField(help_text='password', max_length=50)),
                ('mobile', models.BigIntegerField(help_text='mobile')),
                ('location', models.CharField(help_text='location', max_length=200)),
                ('dob', models.DateField(help_text='dob')),
                ('user_image', models.ImageField(upload_to='user_image')),
                ('reg_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'user_details',
            },
        ),
    ]
