# basic URL Configurations
from django.urls import include, path

# import routers
from rest_framework import routers

# import everything from views
from .views import JobDescriptionViewSet, ResumeViewSet, WorldViewSet

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r"job-description", JobDescriptionViewSet)

router.register(r"resume-upload", ResumeViewSet)

router.register(r"world", WorldViewSet, basename="world")

# specify URL Path for rest_framework
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
