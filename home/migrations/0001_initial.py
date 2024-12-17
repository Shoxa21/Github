# Generated by Django 5.1.4 on 2024-12-17 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1000)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('smtp_server', models.CharField(max_length=100)),
                ('smtp_email', models.CharField(max_length=100)),
                ('smtp_password', models.CharField(max_length=100)),
                ('smtp_port', models.CharField(max_length=100)),
                ('youtube', models.CharField(max_length=100)),
                ('instagram', models.CharField(max_length=100)),
                ('facebook', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='images/settings/')),
                ('about_us', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
            ],
        ),
    ]