# Generated by Django 4.1 on 2022-08-20 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0014_alter_tags_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='color',
            field=models.CharField(blank=True, default='#E6C3CD', max_length=7),
        ),
    ]