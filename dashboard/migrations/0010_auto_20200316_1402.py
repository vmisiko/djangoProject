# Generated by Django 2.2.5 on 2020-03-16 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20200316_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawpayouts',
            name='payment_mode',
            field=models.CharField(choices=[('p', 'Paypal'), ('M', 'Mpesa')], max_length=20),
        ),
    ]
