# Generated by Django 3.0.1 on 2019-12-28 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20191224_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='color',
            field=models.CharField(default='', max_length=12),
        ),
    ]
