# Generated by Django 2.2.4 on 2019-08-17 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminTestPapers', '0008_auto_20190817_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
    ]