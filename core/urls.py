from django.urls import path
from .views import DoctorProfileView, SiteSettingsView, FooterView

urlpatterns = [
    path("doctor/", DoctorProfileView.as_view(), name="doctor-profile"),
    path("settings/", SiteSettingsView.as_view(), name="site-settings"),
    path("footer/", FooterView.as_view(), name="footer"),
]


# from django.urls import path, include
# from rest_framework import routers
# from .views import DoctorProfileViewSet

# router = routers.DefaultRouter()
# router.register(r'doctors', DoctorProfileViewSet)

# urlpatterns = [
#     path('api/', include(router.urls)),
# ]
