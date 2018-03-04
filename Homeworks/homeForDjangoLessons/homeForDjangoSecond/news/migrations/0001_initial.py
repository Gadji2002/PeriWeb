# Generated by Django 2.0.2 on 2018-03-04 18:36

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('news_list', models.CharField(max_length=100)),
                ('news_details', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]
