# Generated by Django 2.2.5 on 2020-07-20 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20200720_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawpayouts',
            name='payment_mode',
            field=models.CharField(choices=[('p', 'Paypal'), ('M', 'Mpesa')], max_length=20),
        ),
    ]
