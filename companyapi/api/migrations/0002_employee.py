# Generated by Django 5.1.3 on 2024-11-08 05:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=10)),
                ('about', models.TextField()),
                ('position', models.CharField(choices=[('manager', 'manager'), ('software developer', 'software developer'), ('project leader', 'project leader')], max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
    ]
