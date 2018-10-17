# Generated by Django 2.1.2 on 2018-10-15 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0110_auto_20181015_1721'),
        ('grants', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grant',
            old_name='status',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='status',
            new_name='active',
        ),
        migrations.RemoveField(
            model_name='grant',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='grant',
            name='team_member_profiles',
        ),
        migrations.AddField(
            model_name='grant',
            name='team_members',
            field=models.ManyToManyField(related_name='grant_teams', to='dashboard.Profile'),
        ),
    ]