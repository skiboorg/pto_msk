# Generated by Django 2.2.7 on 2019-11-30 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20191130_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Стоимость услуги'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='service_img/', verbose_name='Изображение превью (360 x 240)'),
        ),
    ]