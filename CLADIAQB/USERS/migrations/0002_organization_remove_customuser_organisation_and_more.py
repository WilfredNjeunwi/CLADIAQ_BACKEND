# Generated by Django 5.1.1 on 2024-09-04 13:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='organisation',
        ),
        migrations.CreateModel(
            name='UserOrganizationRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('admin', 'Admin'), ('org_user', 'Organization User')], max_length=10)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='USERS.organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'organization')},
            },
        ),
    ]
