# Generated by Django 2.2.6 on 2021-04-21 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_auto_20210412_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linkusergroup',
            old_name='group_id',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='linkusergroup',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='group',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='linkusergroup',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
