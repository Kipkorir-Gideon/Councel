# Generated by Django 3.2.9 on 2022-01-30 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('councelapp', '0010_rename_user_counsellor_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='counsellor',
            old_name='account',
            new_name='user',
        ),
    ]
