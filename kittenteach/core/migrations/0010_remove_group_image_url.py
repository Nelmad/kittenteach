# Generated by Django 2.0.4 on 2018-06-02 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20180602_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='image_url',
        ),
    ]
