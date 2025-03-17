# import viewsets
from rest_framework import viewsets

# import models
from .models import JobDescription

# import local data
from .serializers import JobDescriptionSerializer

# import services
from .services.pdfuploader import pdfuploader


# create a viewset
class JobDescriptionViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = JobDescription.objects.all()

    # specify serializer to be used
    serializer_class = JobDescriptionSerializer


class WorldViewSet(viewsets.ViewSet):
    def list(self, request):
        return pdfuploader()
