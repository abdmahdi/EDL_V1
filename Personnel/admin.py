from django.contrib import admin
from django.contrib.auth import get_user_model
from authemail.admin import EmailUserAdmin
from .models import *


class MyUserAdmin(EmailUserAdmin):
    list_filter = ['is_etudiant','is_personnel']
    fieldsets = (
		(None, {'fields': ('email', 'password','matricule')}),
		('Personal Info', {'fields': ('first_name', 'last_name',)}),
		('Permissions', {'fields': ('is_etudiant','is_active', 'is_staff', 
									   'is_superuser', 'is_verified', 
									   'groups', 'user_permissions')}),
		('Important dates', {'fields': ('last_login', 'date_joined')}),
		('Custom info', {'fields': ('specialite','department','filier','annee','moyenne_s1','moyenne_s2','moyenne_s3','moyenne_s4','moyenne_s5','moyenne_s6','classment')}),
	)
    
        
    

class VerifiedUserAdmin(MyUserAdmin):
    def has_add_permission(self, request):
        return False


admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), MyUserAdmin)
admin.site.register(VerifiedUser, VerifiedUserAdmin)
admin.site.register(OffreLicence)
admin.site.register(OffreMaster)




from .models import EmailSendModel

# Register your models here.
from Etudiant.models import *

class InscriptionLicenceAdminSide(admin.ModelAdmin):
    list_display = ["email","nom","prenom","matricul_bac","bac_anne","moyenne_bac","moyenne_classment","matricul_univ","is_accept"]
    
    
class InscLicenceSpecialite(admin.ModelAdmin):
    list_display= ["nom_prenom","matricule","choix_1","choix_2","choix_3","choix_4","offreLicence"]
    

class InscMasterSpecialite(admin.ModelAdmin):
    list_display= ["nom_prenom","matricule","choix_1","choix_2","choix_3","choix_4","offreMaster"]    

admin.site.register(InscriptionLicense,InscriptionLicenceAdminSide)    

admin.site.register(InscriptionLicenceSpecialite,InscLicenceSpecialite)
admin.site.register(InscriptionMasterSpecialite,InscMasterSpecialite)