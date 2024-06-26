from django.db import models

# Create your models here.

# user register
class userModel(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(help_text='user_name',max_length=50)
    email=models.CharField(help_text=' email', max_length=50)
    password=models.CharField(help_text='password', max_length=50)
    mobile=models.BigIntegerField(help_text='mobile')
    location=models.CharField(help_text='location', max_length=200)
    dob=models.DateField(help_text='dob')
    user_image=models.ImageField(upload_to='user_image')
    otp=models.IntegerField(null=True)
    status=models.CharField(max_length=50,default='pending',null="True")
    reg_date=models.DateField(auto_now_add=True)

    class Meta:
        db_table='user_details'


class file_uploadModel(models.Model):
    file_id=models.AutoField(primary_key=True)

    user_id=models.IntegerField(null=True)
    file=models.FileField(upload_to='user_image/')
    file_name=models.CharField(help_text='file_name',max_length=200)
    file_size=models.BigIntegerField(help_text='file_size',null=True)
    file_type=models.CharField(help_text='file_type',max_length=300)
    otp=models.IntegerField(null=True)
    status=models.CharField(max_length=50,default='pending',null="True")
    file_uploded_date=models.DateField(auto_now_add=True, null=True)

    class Meta:
        db_table='file_details'



        
