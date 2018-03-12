# Generated by Django 2.0.2 on 2018-03-11 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalog',
            options={'verbose_name': 'Каталоги', 'verbose_name_plural': 'Каталогов'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товары', 'verbose_name_plural': 'Товаров'},
        ),
        migrations.AddField(
            model_name='product',
            name='company',
            field=models.CharField(default=True, max_length=50, verbose_name='Название компании'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='cost',
            field=models.PositiveIntegerField(default=0, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateField(default='1970-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=False, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='catalog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Catalog', verbose_name='Каталог'),
        ),
    ]
