# Generated by Django 5.0.6 on 2024-05-15 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_person_slug_alter_person_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='banner',
            field=models.ImageField(blank=True, default='fallback.jpg', upload_to=''),
        ),
    ]
