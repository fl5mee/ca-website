# Generated by Django 4.2.4 on 2024-02-11 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cawebsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('title', models.TextField()),
                ('bio', models.TextField()),
                ('img', models.ImageField(upload_to='team/', verbose_name='image')),
            ],
        ),
    ]
