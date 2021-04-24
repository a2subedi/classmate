# Generated by Django 2.2.6 on 2021-04-21 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notice', '0003_auto_20210421_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouriteNotice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notice.Notice')),
                ('user_ids', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
