# Generated by Django 3.1.3 on 2020-12-02 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20201202_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Produs')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Imagine')),
                ('description', models.TextField(null=True, verbose_name='Caracteristici')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Preț')),
                ('gender', models.CharField(max_length=20, verbose_name='Gen')),
                ('color', models.CharField(max_length=255, verbose_name='Culoare')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Categoria')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
