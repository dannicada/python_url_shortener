# Generated by Django 3.0.1 on 2019-12-29 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20191227_0238'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
