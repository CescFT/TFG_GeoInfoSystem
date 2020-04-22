# Generated by Django 3.0.2 on 2020-04-19 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GeoInfoSystem', '0011_localitzacio_provincia'),
    ]

    operations = [
        migrations.CreateModel(
            name='imatgeLocal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imatge', models.ImageField(upload_to='')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GeoInfoSystem.local')),
            ],
        ),
    ]
