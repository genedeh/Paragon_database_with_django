# Generated by Django 3.2.6 on 2021-08-22 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='username',
            field=models.CharField(max_length=299, null=True, unique=True),
        ),
    ]