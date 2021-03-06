# Generated by Django 3.0.3 on 2020-05-02 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('price', models.FloatField(default=0)),
                ('review_stars', models.IntegerField()),
                ('sample_picture1', models.FileField(upload_to='')),
                ('sample_picture2', models.FileField(upload_to='')),
                ('sample_picture3', models.FileField(upload_to='')),
            ],
        ),
    ]
