# Generated by Django 3.2.8 on 2021-10-08 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taches', '0002_utilisateur'),
    ]

    operations = [
        migrations.AddField(
            model_name='tache',
            name='utilisateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='taches.utilisateur'),
        ),
    ]
