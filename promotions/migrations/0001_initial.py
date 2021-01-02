# Generated by Django 3.1.1 on 2020-10-03 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promotions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('m', 'Monday'), ('t', 'Tuesday'), ('w', 'Wednesday'), ('t', 'Thursday'), ('f', 'Friday'), ('s', 'Saturday'), ('sn', 'Sunday')], max_length=20)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateField(auto_now=True)),
                ('created_by', models.CharField(max_length=200)),
                ('modified_by', models.CharField(max_length=200)),
            ],
        ),
    ]
