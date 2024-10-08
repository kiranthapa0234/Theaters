# Generated by Django 5.1.1 on 2024-10-06 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('video_link', models.TextField()),
                ('type', models.CharField(choices=[('Movie', 'M'), ('Hollywood Movie', 'HM'), ('TV Show', 'TVS'), ('Sport', 'Sp')], max_length=100)),
            ],
        ),
    ]
