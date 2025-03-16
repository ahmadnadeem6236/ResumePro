# import viewsets
from rest_framework import viewsets

from .models import GeeksModel

# import local data
from .serializers import GeeksSerializer

# import services
from .services.pdfuploader import pdfuploader


# create a viewset
class GeeksViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = GeeksModel.objects.all()

    # specify serializer to be used
    serializer_class = GeeksSerializer


class WorldViewSet(viewsets.ViewSet):
    def list(self, request):
        return pdfuploader()
