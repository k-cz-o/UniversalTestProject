# Generated by Django 4.0.4 on 2022-05-14 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('excel', '0002_uploadfile_columns_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfile',
            name='summary',
        ),
    ]
