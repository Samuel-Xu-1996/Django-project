# Generated by Django 3.0.2 on 2020-01-22 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Po', models.CharField(max_length=30, verbose_name='P O #')),
                ('Vendor_No', models.CharField(max_length=30, verbose_name='Vendor No.')),
                ('Vendor_Name', models.CharField(max_length=50, verbose_name='Vendor_Name')),
                ('Line', models.CharField(max_length=50, verbose_name='Line #')),
                ('Partno', models.CharField(max_length=50, verbose_name='Partno')),
                ('Partdescr', models.CharField(max_length=50, verbose_name='Partdescr')),
                ('GL_Accountno', models.CharField(max_length=50, verbose_name='GL_Accountno')),
                ('Datepromised', models.DateField(verbose_name='Datepromised')),
                ('Qtyonorder', models.IntegerField(verbose_name='Qtyonorder')),
                ('Price', models.FloatField(verbose_name='Price')),
                ('Line_Amount', models.IntegerField(verbose_name='Line_Amount')),
                ('Requestedby', models.CharField(max_length=100, verbose_name='Requestedby')),
                ('Buyer', models.CharField(max_length=100, verbose_name='Buyer')),
                ('Status', models.CharField(max_length=30, verbose_name='Status')),
                ('Projectno', models.CharField(max_length=100, verbose_name='Projectno')),
                ('Project_Desc', models.CharField(max_length=200, verbose_name='Project_Desc')),
            ],
            options={
                'verbose_name': 'purchase report',
                'verbose_name_plural': 'purchase report',
            },
        ),
    ]
