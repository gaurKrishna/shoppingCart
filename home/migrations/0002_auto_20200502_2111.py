# Generated by Django 3.0.3 on 2020-05-02 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='genre',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='sample_picture1',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='sample_picture2',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='sample_picture3',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
