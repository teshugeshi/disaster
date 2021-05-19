from django.db import models

# Create your models here.
class Area(models.Model):
    code=models.CharField(primary_key=True,max_length=255,)
    name=models.CharField(max_length=255,)
class Data(models.Model):
    disaster_code=models.CharField(primary_key=True,max_length=255,)
    datetime=models.DateTimeField(blank=True, null=True)
    area = models.ForeignKey('Area', models.DO_NOTHING)
    village=models.CharField(max_length=255,)
    category=models.CharField(max_length=255,)
    basicallyIntactSquare=models.FloatField(blank=True, null=True)
    slightDamagedSquare=models.FloatField(blank=True, null=True)
    moderateDamagedSquare=models.FloatField(blank=True, null=True)
    seriousDamagedSquare=models.FloatField(blank=True, null=True)
    destroyedSquare=models.FloatField(blank=True, null=True)
    note=models.CharField(max_length=255,)
    reportingUnit=models.CharField(max_length=255,)