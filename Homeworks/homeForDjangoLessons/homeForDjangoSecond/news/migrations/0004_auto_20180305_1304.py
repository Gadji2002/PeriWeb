# Generated by Django 2.0.2 on 2018-03-05 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20180305_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='news_list',
            field=models.CharField(max_length=300, verbose_name='Описание'),
        ),
    ]