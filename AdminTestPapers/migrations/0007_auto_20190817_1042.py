# Generated by Django 2.2.4 on 2019-08-17 10:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminTestPapers', '0006_auto_20190817_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 17, 10, 42, 26, 219997), verbose_name='date published'),
        ),
    ]
