from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser
from .email import *

Department_choice = (('Informatique','Informatique'),
                     ('SCIENCES HUMAINES','SCIENCES HUMAINES'),
                     ('SCIENCES SOCIALES','SCIENCES SOCIALES'),
                     ('SCIENCES ECONOMIQUES','SCIENCES ECONOMIQUES'),
                     )

class Users(EmailAbstractUser):
    is_etudiant = models.BooleanField(default=True)
    is_personnel = models.BooleanField(default=False)
    specialite = models.CharField(choices=Department_choice,default='Informatique',max_length=200)
    department = models.CharField(max_length=10,default="NTIC")
    filier = models.CharField(max_length=10,default="")
    matricule = models.IntegerField(unique=True,default=0000000000)
    annee = models.CharField(max_length=10,default="")
    moyenne_s1 = models.FloatField(default=None,null=True)
    moyenne_s2 = models.FloatField(default=None,null=True)
    moyenne_s3 = models.FloatField(default=None,null=True)
    moyenne_s4 = models.FloatField(default=None,null=True)
    moyenne_s5 = models.FloatField(default=None,null=True)
    moyenne_s6 = models.FloatField(default=None,null=True)
    classment = models.FloatField(default=None,null=True)
    objects = EmailUserManager()
    
    # def save(self,*args, **kwargs):
    #     if self.moyenne_s1 == None or self.moyenne_s2==None or self.moyenne_s3==None or self.moyenne_s4 == None:
    #         self.classment ==0
    #     else:
    #         self.classment = (self.moyenne_s1+self.moyenne_s2+self.moyenne_s3+self.moyenne_s4)/4


class VerifiedUserManager(EmailUserManager):
    def get_queryset(self):
        return super(VerifiedUserManager, self).get_queryset().filter(
            is_verified=True)




class VerifiedUser(Users):
    objects = VerifiedUserManager()

    class Meta:
        proxy = True    






class EmailSendModel(models.Model):
    email_to = models.EmailField(max_length=255)
    specialite = models.CharField(max_length=200)
    matricule = models.CharField(max_length=200,blank=True)
    password = models.CharField(max_length=200,blank=True)
    
    def save(self, *args, **kwargs):
        
     send_mail(to_emails=[self.email_to],specialite=self.specialite,matricule=self.matricule,passw=self.password)
            
            
            
            
            
        
def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf','pptx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')



            
class OffreMaster(models.Model):
    title = models.CharField(max_length=200)
    specialite = models.CharField(choices=Department_choice,default='Informatique',max_length=200)
    fichier = models.FileField(upload_to='fileOffreMaster',blank=True,validators=[validate_file_extension])
    def __str__(self):
        return self.title
    
class OffreLicence(models.Model):
    title = models.CharField(max_length=200)
    specialite = models.CharField(choices=Department_choice,default='Informatique',max_length=200)
    fichier = models.FileField(upload_to='fileOffreLicence',blank=True,validators=[validate_file_extension])
    def __str__(self):
        return self.title
    

    
    