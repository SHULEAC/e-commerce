# Generated by Django 3.1.3 on 2020-12-02 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_clothes_shoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Imagine'),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Imagine'),
        ),
    ]