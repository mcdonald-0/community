# Generated by Django 4.0.2 on 2022-04-05 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0020_alter_trackedposts_view_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackedposts',
            name='ip',
            field=models.CharField(max_length=16),
        ),
    ]
