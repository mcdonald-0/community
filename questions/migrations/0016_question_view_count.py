# Generated by Django 4.0.2 on 2022-04-04 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0015_alter_answer_answerer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='view_count',
            field=models.IntegerField(null=True),
        ),
    ]