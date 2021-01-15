# Generated by Django 3.1.5 on 2021-01-15 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210115_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(null=True, upload_to='products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(null=True, upload_to='products'),
        ),
    ]