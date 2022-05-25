from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.generics import *
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from authemail import wrapper
from Personnel.models import *
# Create your views here.

class InscriptionLicenceView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = InscriptionLicenceSerializers
    queryset = InscriptionLicense.objects.all()


class InscLicenceSpecialiteView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = InscLicenceSpecialiteSerializers
    queryset = InscriptionLicenceSpecialite.objects.all()
    


class InscMasterSpecialiteView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = InscMasterSpecialiteSerializers
    queryset = InscriptionMasterSpecialite.objects.all()
    

  


