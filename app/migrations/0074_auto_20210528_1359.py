# Generated by Django 2.2.4 on 2021-05-28 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0073_auto_20210528_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='opis',
            field=models.TextField(default='Uzupełnij opis aby Twój profil cieszył się większą popularnością.', max_length='500'),
        ),
    ]
