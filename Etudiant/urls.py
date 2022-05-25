from Personnel.views import  *
from .views import *
from django.urls import *

urlpatterns = [
    path('InscriptionLicence/',InscriptionLicenceView.as_view(),name="Inscription Licence"),
    path('InscriptionLicenceSpecialite/',InscLicenceSpecialiteView.as_view(),name="Inscription Licence Specialite"),
    path('InscriptionMasterSpecialite/',InscMasterSpecialiteView.as_view(),name="Inscription Master Specialite"),

    
]
