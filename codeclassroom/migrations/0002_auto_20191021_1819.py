# Generated by Django 2.2.6 on 2019-10-21 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeclassroom', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Assignments',
            new_name='Assignment',
        ),
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
        migrations.RenameModel(
            old_name='Respopnse',
            new_name='Response',
        ),
        migrations.AlterModelOptions(
            name='classroom',
            options={'verbose_name': 'ClassRoom', 'verbose_name_plural': 'ClassRooms'},
        ),
    ]
