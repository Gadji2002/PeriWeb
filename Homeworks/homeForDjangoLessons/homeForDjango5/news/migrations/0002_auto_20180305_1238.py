# Generated by Django 2.0.2 on 2018-03-05 09:38

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='article',
            name='news_details',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='подробности'),
        ),
        migrations.AlterField(
            model_name='article',
            name='news_list',
            field=models.CharField(max_length=100, verbose_name='Описание'),
        ),
    ]
