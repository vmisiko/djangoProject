# Generated by Django 2.2.5 on 2020-06-28 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email_notify_admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=50, null=True)),
                ('message', models.CharField(blank=True, max_length=500, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='withdrawpayouts',
            name='payment_mode',
            field=models.CharField(choices=[('p', 'Paypal'), ('M', 'Mpesa')], max_length=20),
        ),
    ]
