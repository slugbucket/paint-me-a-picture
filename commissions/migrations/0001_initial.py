# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-01 10:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CommissionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('days_to_complete', models.IntegerField(default=3)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('fullname', models.CharField(max_length=128)),
                ('contact_address', models.CharField(max_length=128)),
                ('due_date', models.DateField(verbose_name='date for customer delivery')),
                ('commission_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='commissions.CommissionType')),
            ],
        ),
        migrations.AddField(
            model_name='commission',
            name='commission_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commissions.CommissionType'),
        ),
        migrations.AddField(
            model_name='commission',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commissions.Request'),
        ),
    ]