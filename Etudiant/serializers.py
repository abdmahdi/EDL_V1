from .models import *
from rest_framework import serializers
from Personnel.models import *



class InscriptionLicenceSerializers(serializers.ModelSerializer):
    class Meta:
        model = InscriptionLicense
        fields = ["email","nom","prenom","specialite","filier","matricul_bac","bac_anne","moyenne_bac","note_math","note_phy",'fichier']
        


class InscLicenceSpecialiteSerializers(serializers.ModelSerializer):
    # offre = serializers.SlugRelatedField(many=True, read_only=True,slug_field='title')
    

    class Meta:
        model = InscriptionLicenceSpecialite
        fields = ["id","nom_prenom","matricule","choix_1","choix_2","choix_3","choix_4","offreLicence"]
        

class InscMasterSpecialiteSerializers(serializers.ModelSerializer):
    # offre = serializers.SlugRelatedField(many=True, read_only=True,slug_field='title')
    

    class Meta:
        model = InscriptionMasterSpecialite
        fields = ["id","nom_prenom","matricule","choix_1","choix_2","choix_3","choix_4","offreMaster"]        