# Generated by Django 3.1.1 on 2020-10-07 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, default='None', max_length=200)),
                ('signin_time', models.DateTimeField(blank=True)),
                ('signout_time', models.DateTimeField(blank=True)),
            ],
        ),
    ]
