# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hackathon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=1024)),
                ('Hackathon', models.ForeignKey(to='app.Hackathon')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email_address', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='members',
            field=models.ManyToManyField(to='app.User'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(related_name='member', to='app.User'),
        ),
    ]
