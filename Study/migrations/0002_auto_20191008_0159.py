# Generated by Django 2.2.4 on 2019-10-08 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Study', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='status',
            field=models.CharField(choices=[('in_progress', 'In Progress'), ('planning', 'Planning'), ('complete', 'Complete')], default='planning', max_length=32),
        ),
    ]
