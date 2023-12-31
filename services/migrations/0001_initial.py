# Generated by Django 3.2.7 on 2022-01-25 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emp_app', '0006_project_project_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply_project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_price', models.IntegerField()),
                ('applied_duration', models.CharField(max_length=10)),
                ('applied_Date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('applied_status', models.BooleanField(blank=True, default=False, null=True)),
                ('applied_developer_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apllied_dev_developerid', to=settings.AUTH_USER_MODEL)),
                ('applied_project_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied_projectid', to='emp_app.project')),
            ],
        ),
        migrations.CreateModel(
            name='Alloted_projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alloted_price', models.IntegerField(blank=True, null=True)),
                ('alloted_duration', models.CharField(blank=True, max_length=10, null=True)),
                ('alloted_Date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('alloted_project_status', models.BooleanField(blank=True, default=False, null=True)),
                ('alloted_developer_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alloted_dev_developerid', to=settings.AUTH_USER_MODEL)),
                ('alloted_project_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alloted_projectid', to='emp_app.project')),
            ],
        ),
    ]
