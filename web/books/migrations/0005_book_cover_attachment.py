# Generated by Django 3.0.1 on 2019-12-22 19:22

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20181215_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_attachment',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, help_text='Trello card attachment info. See https://developers.trello.com/reference#cardsidattachments.'),
        ),
    ]
