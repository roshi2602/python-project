# Generated by Django 3.1.1 on 2020-10-12 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_rest_passwordreset', '0003_allow_blank_and_null_fields'),
        ('authtoken', '0003_tokenproxy'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]