# Generated by Django 4.0.2 on 2022-02-16 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_userprofile_options_userprofile_created_at_and_more'),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='questioner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.userprofile'),
        ),
    ]