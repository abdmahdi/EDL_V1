# Generated by Django 4.0.4 on 2022-05-25 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Personnel', '0003_alter_users_is_personnel'),
        ('Etudiant', '0003_inscriptionlicencespecialite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscriptionlicencespecialite',
            name='offreLicence',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Personnel.offrelicence'),
        ),
    ]
