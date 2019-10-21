# Generated by Django 2.2.5 on 2019-10-02 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('category', models.CharField(choices=[('s', 'Shirt'), ('sw', 'Sport Wear'), ('OW', 'Outwear')], max_length=1)),
                ('Label', models.CharField(choices=[('S', 'secondaryr'), ('P', 'primary'), ('D', 'danger')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.Item')),
            ],
        ),
    ]
