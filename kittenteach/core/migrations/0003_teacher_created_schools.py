# Generated by Django 2.0.4 on 2018-05-28 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180502_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='created_schools',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='core.School'),
        ),
    ]