# Generated by Django 4.0.6 on 2022-07-14 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_system', '0010_users_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]