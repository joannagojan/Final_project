# Generated by Django 4.1 on 2022-08-28 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0027_alter_event_tags_alter_task_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='urgent',
            field=models.IntegerField(choices=[(1, 'max priority'), (2, 'urgent'), (3, 'not urgent')], default=2),
        ),
    ]
