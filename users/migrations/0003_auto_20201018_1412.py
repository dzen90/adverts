# Generated by Django 3.0.5 on 2020-10-18 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_last_seen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='last_seen',
            new_name='last_visit',
        ),
    ]
