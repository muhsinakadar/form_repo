# Generated by Django 4.1.2 on 2022-10-26 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0002_geeksmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='ToDoList',
        ),
    ]
