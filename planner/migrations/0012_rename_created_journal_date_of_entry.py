# Generated by Django 4.1 on 2022-08-20 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0011_alter_journal_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journal',
            old_name='created',
            new_name='date_of_entry',
        ),
    ]
