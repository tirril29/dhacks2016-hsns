# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Hackathon',
            new_name='hackathon',
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='DEP Title', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(default='I', max_length=1, choices=[(b'I', b'IDEA'), (b'L', b'LESS')]),
            preserve_default=False,
        ),
    ]
