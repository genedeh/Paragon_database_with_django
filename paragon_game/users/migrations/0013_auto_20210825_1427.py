# Generated by Django 3.2.3 on 2021-08-25 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20210825_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='capturer',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='capturer', to='users.player'),
        ),
        migrations.AlterField(
            model_name='group',
            name='defender',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='defender', to='users.player'),
        ),
        migrations.AlterField(
            model_name='group',
            name='middlemen',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='middlemen', to='users.player'),
        ),
    ]
