# Generated by Django 3.2.8 on 2021-10-08 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taches', '0003_tache_utilisateur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tache',
            name='complete',
        ),
    ]
