# Generated by Django 2.0.3 on 2018-03-22 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='kind',
            field=models.CharField(choices=[('h', 'Хищник'), ('t', 'Травоядное'), ('v', 'Всеядное')], max_length=1, verbose_name='Вид'),
        ),
    ]
