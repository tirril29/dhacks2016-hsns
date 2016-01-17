# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160117_0647'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(default='#evil', max_length=1024),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.BooleanField(),
        ),
    ]
