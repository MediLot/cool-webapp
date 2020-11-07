from django.db import models

# Create your models here.


class user_info(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.user_name

class csv_file(models.Model):
    file_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(user_info,on_delete=models.CASCADE)
    file_name = models.CharField(max_length=50,unique=True)
    file_save = models.CharField(max_length=50,unique=True)

class analysis(models.Model):
    analysis_id = models.AutoField(primary_key=True)
    analysis_name = models.CharField(max_length=50,unique=True)
    analysis_save = models.CharField(max_length=50, unique=True)
    file_id = models.ForeignKey(csv_file,on_delete=models.CASCADE)
    analysis_type = models.CharField(max_length=50)