# Generated by Django 3.0.3 on 2020-05-03 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200502_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=200000),
        ),
        migrations.AlterField(
            model_name='product',
            name='review_stars',
            field=models.CharField(max_length=1),
        ),
    ]