# Generated by Django 3.2.12 on 2023-12-04 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_count',
            field=models.IntegerField(default=0),
        ),
    ]
