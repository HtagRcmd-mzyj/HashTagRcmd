# Generated by Django 3.2.14 on 2022-10-31 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KeyBERTModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_text', models.TextField(default='')),
                ('hashtag', models.TextField(default='')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
