# Generated by Django 3.2.2 on 2021-05-07 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remove_child_model', '0002_child'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Child',
        ),
    ]
