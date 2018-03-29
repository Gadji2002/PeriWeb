# Generated by Django 2.0.3 on 2018-03-25 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20180322_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('kind', models.CharField(choices=[('h', 'Хищник'), ('t', 'Травоядное'), ('v', 'Всеядный')], max_length=1, verbose_name='Вид')),
                ('img', models.ImageField(blank=True, null=True, upload_to='news', verbose_name='Изображение')),
            ],
        ),
        migrations.DeleteModel(
            name='Animal',
        ),
    ]
