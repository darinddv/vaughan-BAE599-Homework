# Generated by Django 4.1.2 on 2022-10-13 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=200)),
                ('date_planted', models.DateTimeField(verbose_name='date planted')),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('observation_content', models.CharField(max_length=1000)),
                ('observation_type', models.CharField(choices=[('weather', 'Weather'), ('crop', 'Crop'), ('soil', 'Soil'), ('water', 'Water'), ('pest', 'Pest'), ('other', 'Other')], max_length=200)),
                ('observation_title', models.DateTimeField()),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmnotes.field')),
            ],
        ),
    ]