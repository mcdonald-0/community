# Generated by Django 4.0.2 on 2022-04-06 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0023_alter_trackedposts_options_trackedposts_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='view_count',
        ),
    ]