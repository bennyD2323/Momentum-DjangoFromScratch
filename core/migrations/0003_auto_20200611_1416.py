# Generated by Django 3.0.6 on 2020-06-11 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200606_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codesnippet',
            name='language',
            field=models.CharField(choices=[('HTML', 'HTML'), ('CSS', 'CSS'), ('JAVASCRIPT', 'JavaScript'), ('PYTHON', 'Python')], default='HTML', max_length=30),
        ),
    ]
