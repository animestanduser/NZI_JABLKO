# Generated by Django 2.2.19 on 2021-03-19 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20210319_0953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='nauczyciel',
            new_name='korepetytor',
        ),
    ]
