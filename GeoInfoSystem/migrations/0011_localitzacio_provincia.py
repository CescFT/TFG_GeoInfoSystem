# Generated by Django 3.0.2 on 2020-03-20 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeoInfoSystem', '0010_auto_20200320_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='localitzacio',
            name='provincia',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
