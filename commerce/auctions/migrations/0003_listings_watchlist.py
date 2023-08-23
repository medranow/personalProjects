# Generated by Django 4.1.6 on 2023-02-21 18:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bids_category_comments_listings'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='watchlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
