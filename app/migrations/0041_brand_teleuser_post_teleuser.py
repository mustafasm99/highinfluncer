# Generated by Django 4.0.6 on 2022-10-21 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_item_offer_admin_accept_requests_admin_accept'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='teleuser',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='teleuser',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
