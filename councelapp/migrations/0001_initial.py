# Generated by Django 3.2.9 on 2022-01-27 05:51

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='councelapp.clientprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Counsellor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('experience', models.CharField(max_length=200)),
                ('qualities', models.TextField(max_length=200)),
                ('tel_no', models.IntegerField()),
                ('clients', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='councelapp.clientprofile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True)),
                ('time', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('conversation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='councelapp.conversation')),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True, unique=True)),
                ('bio', models.TextField(null=True)),
                ('admin', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('clients', models.ManyToManyField(to='councelapp.ClientProfile')),
            ],
        ),
        migrations.CreateModel(
            name='CounselorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=300)),
                ('profile_pic', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('counselor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='counselor', to='councelapp.counsellor')),
            ],
        ),
        migrations.CreateModel(
            name='Counselling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_contacted', models.DateField(default=django.utils.timezone.now)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='councelapp.clientprofile')),
                ('counsellor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='councelapp.counsellor')),
            ],
            options={
                'ordering': ['-date_contacted'],
            },
        ),
        migrations.AddField(
            model_name='conversation',
            name='counsellor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='councelapp.counsellor'),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='counsellor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='counsellor', to='councelapp.counsellor'),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
