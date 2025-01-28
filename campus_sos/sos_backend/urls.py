# sos_backend/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LocationViewSet, SOSAlertView, NearestCrowdedLocationView, MatchBuddyView
from . import views
router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Includes all the routes defined by the router
]
# sos_backend/urls.py

urlpatterns = [
    path('sos_alert/', views.SOSAlertView.as_view(), name='sos_alert'),
]

urlpatterns = [
    path('update-location/', views.update_location, name='update-location'),
]
# sos_backend/urls.py

urlpatterns = [
    path('nearest_crowded_location/', views.NearestCrowdedLocationView.as_view(), name='nearest_crowded_location'),
]

# sos_backend/urls.py

urlpatterns = [
    path('match_buddy/', views.MatchBuddyView.as_view(), name='match_buddy'),
]


