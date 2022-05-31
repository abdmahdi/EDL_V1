from django.contrib.auth import get_user_model
from rest_framework import serializers
from Etudiant.models import *
from Personnel.models import *


class MyUserSerializer(serializers.ModelSerializer):
    """
    Write your own User serializer.
    """
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')


class MyUserChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name')
        

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["email","first_name","last_name","password"]

class UsersViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["email","first_name","last_name","matricule"]
        

class UserViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["email","first_name","last_name","matricule","department","filier","moyenne_s1","moyenne_s2","moyenne_s3","moyenne_s4"]
                
        

class ListInscriptionLicenceSerializers(serializers.ModelSerializer):
    class Meta:
        model    = InscriptionLicense
        exclude = ["is_accept"]    
        
class EmailSendSerializers(serializers.ModelSerializer):
   
   class Meta:
       model = EmailSendModel
       fields = "__all__"
    
class OffreMasterSerializers(serializers.ModelSerializer):
       
   class Meta:
       model = OffreMaster
       fields = "__all__"
    
class OffreLicenceSerializers(serializers.ModelSerializer):
       
   class Meta:
       model = OffreLicence
       fields = "__all__"
    