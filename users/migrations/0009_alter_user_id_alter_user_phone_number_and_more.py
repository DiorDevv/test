# Generated by Django 5.1.5 on 2025-02-04 17:50

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='userconfirmation',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='userconfirmation',
            name='verify_type',
            field=models.CharField(choices=[('via_phone_number', 'via_phone_number'), ('via_email', 'via_email')], default='code_verified', max_length=19),
        ),
    ]
