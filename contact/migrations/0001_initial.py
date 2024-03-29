# Generated by Django 3.0.1 on 2022-09-20 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=256)),
                ('message_content', models.TextField()),
            ],
        ),
    ]
