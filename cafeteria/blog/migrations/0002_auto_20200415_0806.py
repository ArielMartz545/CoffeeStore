# Generated by Django 3.0.4 on 2020-04-15 14:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 15, 14, 6, 33, 183861, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
    ]
