# Generated by Django 3.1.7 on 2021-05-18 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_manage', '0002_auto_20210518_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('disaster_code', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('village', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('basicallyIntactSquare', models.FloatField(blank=True, null=True)),
                ('slightDamagedSquare', models.FloatField(blank=True, null=True)),
                ('moderateDamagedSquare', models.FloatField(blank=True, null=True)),
                ('seriousDamagedSquare', models.FloatField(blank=True, null=True)),
                ('destroyedSquare', models.FloatField(blank=True, null=True)),
                ('note', models.CharField(max_length=255)),
                ('reportingUnit', models.CharField(max_length=255)),
            ],
        ),
    ]