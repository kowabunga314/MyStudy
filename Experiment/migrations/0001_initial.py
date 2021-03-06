# Generated by Django 2.2.4 on 2019-10-08 01:59

import NoX.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Base', '0001_initial'),
        ('Study', '0002_auto_20191008_0159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Study.Study', to_field='id')),
            ],
        ),
        migrations.CreateModel(
            name='ExperimentField',
            fields=[
                ('basefield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Base.BaseField')),
                ('text_value', models.CharField(default=None, max_length=255)),
                ('numeric_value', models.DecimalField(decimal_places=15, default=None, max_digits=15)),
                ('dropdown_options', NoX.fields.DropdownField(default=None)),
                ('checkbox_value', models.BooleanField(default=False)),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Experiment.Experiment')),
                ('study_field', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Study.StudyField')),
            ],
            bases=('Base.basefield',),
        ),
    ]
