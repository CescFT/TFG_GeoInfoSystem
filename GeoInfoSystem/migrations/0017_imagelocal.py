# Generated by Django 3.0.2 on 2020-04-26 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GeoInfoSystem', '0016_auto_20200424_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='imageLocal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imatge', models.ImageField(upload_to='photo')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GeoInfoSystem.local')),
            ],
        ),
    ]
