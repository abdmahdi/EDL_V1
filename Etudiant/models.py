from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from Personnel.models import *

Department_choice = (('Informatique','Informatique'),
                     ('SCIENCES HUMAINES','SCIENCES HUMAINES'),
                     ('SCIENCES SOCIALES','SCIENCES SOCIALES'),
                     ('SCIENCES ECONOMIQUES ','SCIENCES ECONOMIQUES '),
                    #  ('SPORT','SPORT'),
                     )



Filier_choice = (('Techniques Mathématiques','Techniques Mathématiques'),
                     ('Sciences Expérimentales','Sciences Expérimentales'),
                     ('Mathématiques','Mathématiques'),
                     ('Latters et Philosophie ','Latters et Philosophie'),
                     ('Langues Etrangéres','Langues Etrangéres'),
                     ('Gestion et Economie','Gestion et Economie'),
                     )


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
    
class InscriptionLicense(models.Model):
    
    
    class InscriptionLicenseObjects(models.Manager):
            def get_queryset(self):
             return super().get_queryset().filter(is_accept=True)
    
    email = models.EmailField(max_length=255,unique=True,blank=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    specialite = models.CharField(choices=Department_choice,default='Informatique',max_length=200)
    filier = models.CharField(choices=Filier_choice,max_length=200,default="Mathématiques")
    matricul_bac = models.IntegerField(unique=True)
    bac_anne = models.IntegerField()
    moyenne_bac = models.FloatField()
    note_math = models.FloatField(blank=True,null=True)
    note_phy = models.FloatField(blank=True,null=True)
    fichier = models.FileField(upload_to='fileInscriptionLicence',blank=True,validators=[validate_file_extension])
    moyenne_classment = models.FloatField(blank=True,null=True)
    matricul_univ = models.IntegerField(blank=True)
    is_accept = models.BooleanField(default=False)
    perioriter = models.IntegerField(blank=True,default=1)
    objects = models.Manager()  # default manager
    postobjects = InscriptionLicenseObjects() 
    
    
    class Meta:
        ordering = ('-perioriter',)

    
    
    def __str__(self):
        return self.nom + "   " +self.prenom
    
    def save(self, *args, **kwargs):
        if self.note_math is not None and self.note_phy is not None:
            self.moyenne_classment = (self.moyenne_bac*2+(self.note_math+self.note_phy)/2)/3
            
        matricull = self.bac_anne-2000
        matricul = f"{matricull}{matricull}{self.matricul_bac}"
        self.matricul_univ = int(matricul)
        if self.specialite == "Informatique":
            if self.filier == "Techniques Mathématiques" or self.filier == "Mathématiques":
                self.perioriter = 1
            else:
                self.perioriter = 2
        if self.specialite == "SCIENCES HUMAINES":
            if self.filier == "Latters et Philosophie" or self.filier == "Langues Etrangéres":
                self.perioriter = 1
            else: 
                self.perioriter = 2    
            
        if self.specialite == "SCIENCES SOCIALES"   :
            if self.filier == "Latters et Philosophie"  or self.filier == "Langues Etrangéres"  :
                self.perioriter = 1
            else:
                self.perioriter = 2    
        if self.specialite =="SCIENCES ECONOMIQUES":
            if self.filier == "Gestion et Economie":
                self.perioriter =1
            else:
                self.perioriter = 2    
                
        annee_accept = 2022-self.bac_anne
        if 0 <=annee_accept <=5:
            if self.specialite == "Informatique" and self.moyenne_bac >=13.20:
              self.is_accept = True
            if self.specialite == "SCIENCES HUMAINES" and self.moyenne_bac>=10:
                self.is_accept = True
            if self.specialite == "SCIENCES SOCIALES" and self.moyenne_bac>=10:
                self.is_accept = True
            if self.specialite == "SCIENCES ECONOMIQUES" and self.moyenne_bac>=9.50:
                self.is_accept = True
                        
        else:
            self.is_accept = False  
            
              
        super().save(*args, **kwargs)   
    
    
    
    
# class Etudiant(models.Model):


class InscriptionLicenceSpecialite(models.Model):
    offreLicence = models.ForeignKey(OffreLicence,on_delete=models.CASCADE)
    nom_prenom = models.CharField(max_length=200)
    matricule = models.IntegerField()
    choix_1 = models.CharField(max_length=10)
    choix_2 = models.CharField(max_length=10)
    choix_3 = models.CharField(max_length=10)
    choix_4 = models.CharField(max_length=10)



class InscriptionMasterSpecialite(models.Model):
    offreMaster = models.ForeignKey(OffreMaster,on_delete=models.CASCADE)
    nom_prenom = models.CharField(max_length=200)
    matricule = models.IntegerField()
    choix_1 = models.CharField(max_length=10)
    choix_2 = models.CharField(max_length=10)
    choix_3 = models.CharField(max_length=10)
    choix_4 = models.CharField(max_length=10)    
    