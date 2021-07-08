# Generated by Django 3.2.4 on 2021-07-08 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bloodline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=159, unique=True)),
                ('power_level', models.FloatField(unique='True')),
                ('symbol', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('image', models.ImageField(upload_to='')),
                ('power', models.CharField(max_length=359)),
                ('bio', models.TextField()),
                ('bloodline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.bloodline')),
            ],
        ),
    ]
