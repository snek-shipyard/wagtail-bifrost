# Generated by Django 3.1.6 on 2021-03-01 22:15

import bifrost.models.files
from django.db import migrations, models
import private_storage.fields
import private_storage.storage.files


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bifrost', '0003_delete_stubmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BifrostFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(default=bifrost.models.files.generate_key, max_length=40)),
                ('file', private_storage.fields.PrivateFileField(storage=private_storage.storage.files.PrivateFileSystemStorage(), upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
