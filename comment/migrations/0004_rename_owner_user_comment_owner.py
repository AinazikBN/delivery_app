# Generated by Django 5.0.6 on 2024-06-30 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_rename_menu_comment_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='owner_user',
            new_name='owner',
        ),
    ]