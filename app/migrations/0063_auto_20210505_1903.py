# Generated by Django 2.2.19 on 2021-05-05 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0062_auto_20210505_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ranga',
            field=models.CharField(choices=[('brak', 'Brak (0-1199)'), ('wood', 'Wood (1200-1399)'), ('leaf', 'Leaf (1400-1599)'), ('gold', 'Gold (1600-1799)'), ('diamond', 'Diamond (1800-)')], default='brak', max_length=30),
        ),
    ]
