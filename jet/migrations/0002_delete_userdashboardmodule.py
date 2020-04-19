# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import absolute_import
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jet', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserDashboardModule',
        ),
    ]
