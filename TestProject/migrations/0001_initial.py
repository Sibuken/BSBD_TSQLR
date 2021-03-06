# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-03 11:59
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Answer', models.TextField(max_length=30000)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ConnectDataBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameConnection', models.CharField(max_length=10)),
                ('ConnectionString', models.TextField()),
                ('ShadowConnectionString', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='GP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameGP', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Text', tinymce.models.HTMLField()),
                ('Date', models.DateTimeField(default=datetime.datetime(2017, 6, 3, 11, 59, 4, 522769, tzinfo=utc), editable=False)),
                ('Group', models.ManyToManyField(blank=True, null=True, to='TestProject.GP')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameTask', models.CharField(max_length=20)),
                ('TaskText', models.TextField()),
                ('WTask', models.TextField()),
                ('Weight', models.IntegerField()),
                ('Vision', models.BooleanField()),
                ('Category', models.ManyToManyField(to='TestProject.Category')),
                ('ConnectDataBase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestProject.ConnectDataBase')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('DateActivate', models.DateTimeField()),
                ('Time', models.IntegerField()),
                ('HardCheck', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TestConnectDataBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ConnectDataBase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestProject.ConnectDataBase')),
                ('Test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestProject.Test')),
            ],
        ),
        migrations.CreateModel(
            name='TestPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mark', models.FloatField(blank=True, null=True)),
                ('StartTest', models.DateTimeField(blank=True, null=True)),
                ('Variant', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TestTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Variant', models.IntegerField()),
                ('Task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestProject.Task')),
                ('Test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestProject.Test')),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('GP', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TestProject.GP')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='testperson',
            name='Person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='testperson',
            name='Test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestProject.Test'),
        ),
        migrations.AddField(
            model_name='test',
            name='Task',
            field=models.ManyToManyField(through='TestProject.TestTask', to='TestProject.Task'),
        ),
        migrations.AddField(
            model_name='test',
            name='TestPerson',
            field=models.ManyToManyField(through='TestProject.TestPerson', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answers',
            name='TestPerson',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='TestProject.TestPerson'),
        ),
        migrations.AddField(
            model_name='answers',
            name='TestTask',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestProject.TestTask'),
        ),
    ]
