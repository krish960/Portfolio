# Generated by Django 5.1.5 on 2025-01-30 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anmins', '0003_about_me'),
    ]

    operations = [
        migrations.CreateModel(
            name='ABOUT_INFO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profile', models.CharField(max_length=100)),
                ('Education', models.CharField(max_length=100)),
                ('Language', models.CharField(max_length=100)),
                ('Tools', models.CharField(max_length=100)),
                ('O_Skills', models.CharField(max_length=100)),
                ('Interest', models.CharField(max_length=100)),
                ('Projects_completed', models.CharField(max_length=100)),
            ],
        ),
    ]
