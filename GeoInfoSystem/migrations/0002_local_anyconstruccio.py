# Generated by Django 3.0.2 on 2020-02-02 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeoInfoSystem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='anyConstruccio',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
