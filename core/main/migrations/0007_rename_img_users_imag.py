# Generated by Django 4.0.5 on 2022-06-16 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_users_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='img',
            new_name='imag',
        ),
    ]
