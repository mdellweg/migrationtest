# Generated by Django 3.2.2 on 2021-05-07 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('remove_child_model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('parent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='remove_child_model.parent')),
                ('alias', models.TextField()),
            ],
            bases=('remove_child_model.parent',),
        ),
    ]
