# Generated by Django 3.2.9 on 2022-02-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('councelapp', '0023_alter_chat_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='Text',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='Text',
        ),
    ]
