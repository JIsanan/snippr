# Generated by Django 2.1.1 on 2018-10-23 05:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('snippr', '0009_auto_20181023_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]