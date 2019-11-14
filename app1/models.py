from django.db import models

class Sample(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
