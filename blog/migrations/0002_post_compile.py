# Generated by Django 3.0.3 on 2020-04-25 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='compile',
            field=models.BooleanField(default=False),
        ),
    ]
