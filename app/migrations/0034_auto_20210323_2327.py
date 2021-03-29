# Generated by Django 2.2.19 on 2021-03-23 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0033_auto_20210323_2326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='author',
        ),
        migrations.AddField(
            model_name='report',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
