# Generated by Django 4.2.16 on 2024-11-30 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_rename_earings_cardealer_earnings"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cardealer",
            name="location",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="home.location"
            ),
        ),
    ]