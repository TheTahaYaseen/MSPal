# Generated by Django 4.2.6 on 2023-12-08 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pal', '0002_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('associated_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pal.subject')),
            ],
        ),
        migrations.CreateModel(
            name='TopicRevision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('associated_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pal.topic')),
            ],
        ),
    ]
