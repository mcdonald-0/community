# Generated by Django 4.0.2 on 2022-04-28 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_alter_reportedissue_issue_in_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportedissue',
            old_name='ip_address_reported_from',
            new_name='reporter_ip_address',
        ),
    ]
