# Generated by Django 3.0.3 on 2020-04-17 17:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('strain_stock', '0003_auto_20200410_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='strainoperation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
