# Generated by Django 4.1.4 on 2023-01-04 02:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpost_blogmonth_blogpost_blogyear_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blogDateTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 3, 21, 29, 49, 733541)),
        ),
    ]