# Generated by Django 3.1.3 on 2020-12-28 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20201228_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='final_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='În total'),
        ),
    ]
