# Generated by Django 4.0.4 on 2022-05-24 23:03

import Etudiant.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Etudiant', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inscriptionlicense',
            options={'ordering': ('-perioriter',)},
        ),
        migrations.AddField(
            model_name='inscriptionlicense',
            name='email',
            field=models.EmailField(blank=True, max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='inscriptionlicense',
            name='fichier',
            field=models.FileField(blank=True, upload_to='fileInscriptionLicence', validators=[Etudiant.models.validate_file_extension]),
        ),
        migrations.AddField(
            model_name='inscriptionlicense',
            name='filier',
            field=models.CharField(choices=[('Techniques Mathématiques', 'Techniques Mathématiques'), ('Sciences Expérimentales', 'Sciences Expérimentales'), ('Mathématiques', 'Mathématiques'), ('Latters et Philosophie ', 'Latters et Philosophie'), ('Langues Etrangéres', 'Langues Etrangéres'), ('Gestion et Economie', 'Gestion et Economie')], default='Mathématiques', max_length=200),
        ),
        migrations.AddField(
            model_name='inscriptionlicense',
            name='is_accept',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='inscriptionlicense',
            name='perioriter',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='inscriptionlicense',
            name='specialite',
            field=models.CharField(choices=[('Informatique', 'Informatique'), ('SCIENCES HUMAINES', 'SCIENCES HUMAINES'), ('SCIENCES SOCIALES', 'SCIENCES SOCIALES'), ('SCIENCES ECONOMIQUES ', 'SCIENCES ECONOMIQUES ')], default='Informatique', max_length=200),
        ),
        migrations.AlterField(
            model_name='inscriptionlicense',
            name='bac_anne',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inscriptionlicense',
            name='matricul_bac',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='inscriptionlicense',
            name='matricul_univ',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='inscriptionlicense',
            name='moyenne_bac',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inscriptionlicense',
            name='moyenne_classment',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='inscriptionlicense',
            name='note_math',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='inscriptionlicense',
            name='note_phy',
            field=models.FloatField(blank=True),
        ),
    ]
