# Generated by Django 2.2 on 2019-04-14 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moment',
            name='content',
            field=models.CharField(max_length=300),
        ),
    ]
