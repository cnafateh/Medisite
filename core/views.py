from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import DoctorProfile, SiteSettings
from .serializers import (
    DoctorProfileSerializer,
    SiteSettingsSerializer,
    FooterSerializer
)


# ---------------------------
# Doctor Profile View
# ---------------------------
class DoctorProfileView(ListAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer

    # # همیشه اولین پزشک را برمی‌گردانیم
    # def get_object(self):
    #     return DoctorProfile.objects.first()

# ---------------------------
# Site Settings View
# ---------------------------
class SiteSettingsView(ListAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer

    # def get_object(self):
    #     return SiteSettings.objects.first()

# ---------------------------
# Footer View (Combined)
# ---------------------------
class FooterView(APIView):
    def get(self, request):
        settings = SiteSettings.objects.first()
        serializer = FooterSerializer(settings)
        return Response(serializer.data, status=status.HTTP_200_OK)





# from rest_framework import viewsets
# from .models import DoctorProfile
# from .serializers import DoctorProfileSerializer
# from rest_framework.permissions import IsAuthenticated

# class DoctorProfileViewSet(viewsets.ModelViewSet):
#     queryset = DoctorProfile.objects.all()
#     serializer_class = DoctorProfileSerializer
#     permission_classes = [IsAuthenticated]
