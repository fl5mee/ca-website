# Generated by Django 4.2.4 on 2024-02-11 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cawebsite', '0002_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='name (what you want this event to be called in the admin interface)')),
                ('title', models.TextField(verbose_name='title (example: US-UT: Provo)')),
                ('desc', models.TextField(verbose_name='description (example: Evan Smith (Brigham Young University))')),
                ('img', models.ImageField(upload_to='branches/', verbose_name='image')),
            ],
        ),
    ]