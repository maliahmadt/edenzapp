# Generated by Django 5.0.4 on 2024-04-12 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='cnic',
            field=models.CharField(default='', max_length=15, unique=True),
        ),
    ]
