# Generated by Django 3.2.12 on 2023-11-27 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='haslo', max_length=50),
            preserve_default=False,
        ),
    ]
