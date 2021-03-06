# Generated by Django 3.2.3 on 2021-08-23 19:34

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_player_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='location',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
    ]
