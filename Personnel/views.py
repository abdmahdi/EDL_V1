from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import *
from rest_framework.permissions import *
from rest_framework.decorators import *
from rest_framework.response import Response
from rest_framework import status
from Etudiant.models import *
from Etudiant.serializers import *

 
# Create your views here.


# class CreateUser(CreateAPIView):
#     serializer_class = UserSerializers
#     def perform_create(self, serializer):
#             serializer.save(is_active=True,is_verified=True)
#     queryset = Users.objects.all()        



class Alletudiant(ListAPIView):
    serializer_class = UsersViewSerializers
    queryset = Users.objects.filter(is_etudiant = True)  


class etudiantView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserViewSerializers
    queryset = Users.objects.filter(is_etudiant = True)
    def get_object(self):
           matricule= self.kwargs.get("matricule")
           return get_object_or_404(Users.objects.filter(matricule=matricule), matricule=matricule)

    




class MyUserMe(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MyUserSerializer

    def get(self, request, format=None):
        return Response(self.serializer_class(request.user).data)


class MyUserMeChange(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MyUserChangeSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = request.user

            if 'first_name' in serializer.data:
                user.first_name = serializer.data['first_name']
            if 'last_name' in serializer.data:
                user.last_name = serializer.data['last_name']
            if 'date_of_birth' in serializer.data:
                user.date_of_birth = serializer.data['date_of_birth']
            if 'user_name' in serializer.data:
                user.user_name= serializer.data['user_name']    

            user.save()

            content = {'success': ('User information changed.')}
            return Response(content, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ListInscriptionLicenceView(ListAPIView):
    serializer_class = ListInscriptionLicenceSerializers
    permission_classes = [AllowAny]
    queryset =    InscriptionLicense.objects.all() 


#################################################### List View ###################################################################       

class ListInscriptionLicenceInformatiqueView(ListAPIView):
    serializer_class = ListInscriptionLicenceSerializers
    permission_classes = [AllowAny]
    def get_queryset(self):
        return InscriptionLicense.objects.filter(specialite="Informatique",is_accept=True)

class ListInscriptionLicenceSCIENCESHUMAINESView(ListAPIView):
    serializer_class = ListInscriptionLicenceSerializers
    permission_classes = [AllowAny]
    def get_queryset(self):
        return InscriptionLicense.objects.filter(specialite="SCIENCES HUMAINES",is_accept=True)


class ListInscriptionLicenceSCIENCESSOCIALESView(ListAPIView):
    serializer_class = ListInscriptionLicenceSerializers
    permission_classes = [AllowAny]
    def get_queryset(self):
        return InscriptionLicense.objects.filter(specialite="SCIENCES SOCIALES",is_accept=True)        
    

class ListInscriptionLicenceSCIENCESECONOMIQUESView(ListAPIView):
    serializer_class = ListInscriptionLicenceSerializers
    permission_classes = [AllowAny]
    def get_queryset(self):
        return InscriptionLicense.objects.filter(specialite="SCIENCES ECONOMIQUES ",is_accept=True)    
    
#################################################### Signle View ###################################################################    
    
class SingleViewInscrpitonLicenceInformatique(RetrieveAPIView):
     serializer_class = ListInscriptionLicenceSerializers
     permission_classes = [AllowAny]
     def get_queryset(self):
            return InscriptionLicense.objects.filter(specialite="Informatique",is_accept=True)



class SingleViewInscrpitonLicenceSCIENCESHUMAINES(RetrieveAPIView):
     serializer_class = ListInscriptionLicenceSerializers
     permission_classes = [AllowAny]
     def get_queryset(self):
            return InscriptionLicense.objects.filter(specialite="SCIENCES HUMAINES",is_accept=True)



class SingleViewInscrpitonLicenceSCIENCESSOCIALES(RetrieveAPIView):
     serializer_class = ListInscriptionLicenceSerializers
     permission_classes = [AllowAny]
     def get_queryset(self):
            return InscriptionLicense.objects.filter(specialite="SCIENCES SOCIALES",is_accept=True)
        


class SingleViewInscrpitonLicenceSCIENCESECONOMIQUES(RetrieveAPIView):
     serializer_class = ListInscriptionLicenceSerializers
     permission_classes = [AllowAny]
     def get_queryset(self):
            return InscriptionLicense.objects.filter(specialite="SCIENCES ECONOMIQUES ",is_accept=True)                        
     
     
    
####################################################@@###########################@@@@@@@@@@@@@@@#############@@@@@@@@@#############@@@@@@@@##############@@@@@@@########


    


class Emails(CreateAPIView):
    serializer_class = EmailSendSerializers
    queryset = EmailSendModel.objects.all()
   
class OffresLicence(ListAPIView):
    serializer_class = OffreLicenceSerializers
    queryset = OffreLicence.objects.all()
   
class OffresMaster(ListAPIView):
    serializer_class = OffreMasterSerializers
    queryset = OffreMaster.objects.all()
   
class CreateOffreLicence(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = OffreLicenceSerializers
    queryset = OffreLicence.objects.all()
   
class CreateOffreMaster(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = OffreMasterSerializers
    queryset = OffreMaster.objects.all()
 
 


##########################################################@@@@@#####@@@##@#@#@#@##@#@#@@#@#@#@@#@#@@


class ListInscriptionLicenceSpecialite(ListAPIView):
    serializer_class = InscLicenceSpecialiteSerializers
    queryset = InscriptionLicenceSpecialite.objects.all()


class ListInscriptionMasterSpecialite(ListAPIView):
    serializer_class = InscMasterSpecialiteSerializers
    queryset = InscriptionMasterSpecialite.objects.all()     



class SingleViewInscriptionLicenceSpecialite(APIView):
    serializer_class = InscLicenceSpecialiteSerializers
    queryset = InscriptionLicenceSpecialite.objects.all()
    def get_object(self):
           matricule= self.kwargs.get("matricule")
           return get_object_or_404(Users.objects.filter(matricule=matricule), matricule=matricule)


class SingleViewInscriptionMasterSpecialite(APIView):
    serializer_class = InscMasterSpecialiteSerializers
    queryset = InscriptionMasterSpecialite.objects.all()      
    def get_object(self):
           matricule= self.kwargs.get("matricule")
           return get_object_or_404(Users.objects.filter(matricule=matricule), matricule=matricule)  