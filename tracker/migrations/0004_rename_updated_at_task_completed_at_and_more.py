# Generated by Django 4.1 on 2022-08-06 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_team_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='updated_at',
            new_name='completed_at',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='month',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='team_members',
            new_name='team_member',
        ),
    ]
