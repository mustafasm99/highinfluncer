# Generated by Django 4.1.2 on 2022-11-04 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0044_tags_influencer_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='influencer',
            name='engagemantRate',
            field=models.FloatField(blank=True, null=True),
        ),
    ]