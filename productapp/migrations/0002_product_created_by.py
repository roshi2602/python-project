# Generated by Django 3.1.1 on 2020-10-06 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_by',
            field=models.CharField(default='', max_length=200),
        ),
    ]
