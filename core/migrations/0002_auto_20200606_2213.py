# Generated by Django 3.0.6 on 2020-06-06 22:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codesnippet',
            name='tags',
            field=models.ManyToManyField(related_name='snippets', to='core.Tag'),
        ),
        migrations.AlterField(
            model_name='codesnippet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to=settings.AUTH_USER_MODEL),
        ),
    ]