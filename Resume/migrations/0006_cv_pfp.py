# Generated by Django 4.0.5 on 2022-11-21 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0005_remove_cv_pfp'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='Pfp',
            field=models.ImageField(default='*err*', upload_to=''),
        ),
    ]