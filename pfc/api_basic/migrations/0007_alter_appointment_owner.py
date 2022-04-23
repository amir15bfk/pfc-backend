# Generated by Django 4.0.4 on 2022-04-23 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_basic', '0006_appointment_created_at_appointment_importance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
