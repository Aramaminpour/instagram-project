# Generated by Django 4.0.4 on 2022-05-17 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0004_alter_myuser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_verify',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
