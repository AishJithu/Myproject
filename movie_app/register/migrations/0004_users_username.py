# Generated by Django 4.2.11 on 2024-04-01 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_remove_users_username_users_is_admin_alter_users_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='username',
            field=models.CharField(default='', max_length=255),
        ),
    ]