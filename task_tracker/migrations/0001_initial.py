# Generated by Django 3.2.6 on 2021-08-16 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300)),
                ('completed_at', models.DateField()),
                ('reminder', models.BooleanField(default=False)),
            ],
        ),
    ]
