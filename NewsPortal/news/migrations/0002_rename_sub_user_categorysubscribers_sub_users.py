# Generated by Django 3.2.8 on 2022-03-11 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorysubscribers',
            old_name='sub_user',
            new_name='sub_users',
        ),
    ]
