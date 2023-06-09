# Generated by Django 3.2.14 on 2022-10-21 05:44

from django.db import migrations, models
import eff_model.models


class Migration(migrations.Migration):

    dependencies = [
        ('eff_model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, upload_to=eff_model.models.upload_to)),
            ],
        ),
        migrations.RemoveField(
            model_name='effmodel',
            name='image',
        ),
        migrations.RemoveField(
            model_name='effmodel',
            name='updated_at',
        ),
    ]
