# Generated by Django 2.2.19 on 2021-05-05 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0061_auto_20210505_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ranga',
            field=models.CharField(default='brak', max_length=30),
        ),
    ]
