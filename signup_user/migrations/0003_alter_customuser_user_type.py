# Generated by Django 3.2.7 on 2022-01-04 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup_user', '0002_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('client', 'client'), ('developer', 'developer')], default='client', max_length=50),
        ),
    ]
