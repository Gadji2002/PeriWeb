# Generated by Django 2.0.3 on 2018-03-29 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('age', models.SmallIntegerField(verbose_name='Возраст')),
                ('birth', models.DateField(blank=True, verbose_name='ДР')),
            ],
        ),
    ]