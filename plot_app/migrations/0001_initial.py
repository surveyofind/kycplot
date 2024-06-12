# Generated by Django 5.0.6 on 2024-06-09 05:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plot_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('site_name', models.TextField(blank=True, null=True)),
                ('site_code', models.TextField(blank=True, null=True)),
                ('image_Cycle_Slip_PLOT', models.ImageField(upload_to='media')),
                ('image_MP_PLOT', models.ImageField(upload_to='media')),
                ('image_Percentage_Observation', models.ImageField(upload_to='media')),
                ('image_TS_PLOT', models.ImageField(upload_to='media')),
                ('coordinates', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corsid', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=50)),
                ('site_name', models.CharField(max_length=100)),
                ('site_code', models.CharField(max_length=10)),
                ('coordinates_of_sites_dms_lat', models.CharField(max_length=50)),
                ('coordinates_of_sites_dms_long', models.CharField(max_length=50)),
                ('coordinates_of_sites_dms_elp_height', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('site_name', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plot_app.state')),
            ],
        ),
    ]
