# Generated by Django 3.0.5 on 2020-10-13 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_seen',
            field=models.DateTimeField(null=True),
        ),
    ]