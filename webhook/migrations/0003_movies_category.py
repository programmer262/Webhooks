# Generated by Django 4.2.3 on 2024-09-07 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webhook', '0002_remove_movies_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webhook.moviecategory'),
            preserve_default=False,
        ),
    ]
