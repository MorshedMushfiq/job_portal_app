# Generated by Django 5.1.1 on 2024-10-04 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_applynowmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobmodel',
            name='create_at',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='jobmodel',
            name='update_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]