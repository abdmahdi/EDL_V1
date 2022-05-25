from django.urls import *
from .views import *
from Etudiant.views import *

urlpatterns = [
    path('user/create/', CreateUser.as_view()),
    path('etudiants/', Alletudiant.as_view()),
    path('etudiants/<int:matricule>/', etudiantView.as_view()),
   path('users/me/', MyUserMe.as_view()),
    path('users/me/change/', MyUserMeChange.as_view()),
    path('listLicenceInscription/',ListInscriptionLicenceView.as_view(),name="List Inscription Licence"),
    path('listLicenceInscription/Informatique/',ListInscriptionLicenceInformatiqueView.as_view(),name="List Inscription Licence Informatique "),
    path('listLicenceInscription/SCIENCESECONOMIQUES/',ListInscriptionLicenceSCIENCESECONOMIQUESView.as_view(),name="List Inscription Licence SCIENCES ECONOMIQUES"),
    path('listLicenceInscription/SCIENCESSOCIALES/',ListInscriptionLicenceSCIENCESSOCIALESView.as_view(),name="List Inscription Licence SCIENCES SOCIALES"),
    path('listLicenceInscription/SCIENCESHUMAINES/',ListInscriptionLicenceSCIENCESHUMAINESView.as_view(),name="List Inscription Licence SCIENCES HUMAINES"),
    
    ####################################################################################
    
    
    path('listLicenceInscription/Informatique/<int:pk>/',SingleViewInscrpitonLicenceInformatique.as_view(),name="List Inscription Licence Informatiqu "),
    path('listLicenceInscription/SCIENCESECONOMIQUES/<int:pk>/',SingleViewInscrpitonLicenceSCIENCESECONOMIQUES.as_view(),name="List Inscription Licence SCIENCES ECONOMIQUES"),
    path('listLicenceInscription/SCIENCESSOCIALES/<int:pk>/',SingleViewInscrpitonLicenceSCIENCESSOCIALES.as_view(),name="List Inscription Licence SCIENCES SOCIALES"),
    path('listLicenceInscription/SCIENCESHUMAINES/<int:pk>/',SingleViewInscrpitonLicenceSCIENCESHUMAINES.as_view(),name="List Inscription Licence SCIENCES HUMAINES"),
    path('email/',Emails.as_view(),name="Send EMAIL"),
    path('createoffreMaster/',CreateOffreMaster.as_view(),name="offreMaster"),
    path('createoffreLicence/',CreateOffreLicence.as_view(),name="offreLicence/"),
    path('offresMaster/',OffresMaster.as_view(),name="offresMaster"),
    path('offresLicence/',OffresLicence.as_view(),name="offresLicence/"),
    
    #########################@@@@@@@@@@@@@###########@@@@@@#######@@@####@@#@#@#@@@@#@#@#@#@@#@#@@#@#@#@@#@#@@#@@
    path('ListLicence/',ListInscriptionLicenceSpecialite.as_view(),name="List Licence Specialite"),
    path('ListMaster/',ListInscriptionMasterSpecialite.as_view(),name="List Master Specialite"),
    path('ListLicence/<int:matricule>/',SingleViewInscriptionLicenceSpecialite.as_view(),name="Signle View Licence Specialite"),
    path('ListMaster/<int:matricule>/',SingleViewInscriptionMasterSpecialite.as_view(),name="Signle View Master Specialite"),
]
