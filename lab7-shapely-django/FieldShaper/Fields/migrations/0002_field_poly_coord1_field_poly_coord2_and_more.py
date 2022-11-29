# Generated by Django 4.1.3 on 2022-11-29 07:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Fields', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='poly_coord1',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='field',
            name='poly_coord2',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='field',
            name='poly_coord3',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
