# Generated by Django 4.0.6 on 2022-09-29 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_shops_items_shops_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='shop',
        ),
        migrations.AddField(
            model_name='shops',
            name='woner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.brand'),
        ),
    ]
