# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_occupation_detail_form'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Occupation_Detail_Form',
            new_name='Occupation_Detail',
        ),
    ]
