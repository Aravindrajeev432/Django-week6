# Generated by Django 4.0.6 on 2022-07-14 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_system', '0008_rename_usercredential_userdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCredential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
            ],
        ),
    ]
