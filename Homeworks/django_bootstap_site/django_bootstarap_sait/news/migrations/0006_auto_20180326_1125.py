# Generated by Django 2.0.3 on 2018-03-26 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_news_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(verbose_name='Слуг'),
        ),
    ]
