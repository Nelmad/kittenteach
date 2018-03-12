# Generated by Django 2.0.3 on 2018-03-12 22:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attended', models.BooleanField()),
            ],
            options={
                'db_table': 'attendance',
            },
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
            ],
            options={
                'db_table': 'balance',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'groups',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Group')),
            ],
            options={
                'db_table': 'lessons',
            },
        ),
        migrations.CreateModel(
            name='LessonTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField()),
                ('time', models.TimeField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Group')),
            ],
            options={
                'db_table': 'lessons_templates',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('type', models.CharField(choices=[(0, 'deposit'), (1, 'withdraw')], max_length=1)),
                ('current_balance', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('balance', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Balance')),
                ('lesson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Lesson')),
            ],
            options={
                'db_table': 'payments',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'students',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'subjects',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('students', models.ManyToManyField(blank=True, related_name='teachers', to='core.Student')),
                ('subjects', models.ManyToManyField(blank=True, related_name='subjects', to='core.Subject')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'teachers',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='students',
            field=models.ManyToManyField(to='core.Student'),
        ),
        migrations.AddField(
            model_name='group',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Subject'),
        ),
        migrations.AddField(
            model_name='group',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Teacher'),
        ),
        migrations.AddField(
            model_name='balance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Student'),
        ),
        migrations.AddField(
            model_name='balance',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Teacher'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Lesson'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Student'),
        ),
    ]
