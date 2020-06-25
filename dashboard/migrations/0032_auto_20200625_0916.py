# Generated by Django 2.2.5 on 2020-06-25 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0031_auto_20200618_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email_notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.CharField(blank=True, max_length=50, null=True)),
                ('buyer', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='withdrawpayouts',
            name='payment_mode',
            field=models.CharField(choices=[('p', 'Paypal'), ('M', 'Mpesa')], max_length=20),
        ),
    ]