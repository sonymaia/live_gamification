# Generated by Django 4.1.7 on 2023-03-14 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0005_logbook_fk_user_alter_logbook_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Logbook',
            new_name='Daily_Record',
        ),
    ]
