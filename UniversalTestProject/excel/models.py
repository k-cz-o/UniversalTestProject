from django.db import models


# Create your models here.
class UploadFile(models.Model):
    uploaded_file = models.FileField()
    columns_list = models.CharField(max_length=250, blank=True)

