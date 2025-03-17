# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import JobDescription, Resume


# Create a model serializer
class ResumeSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Resume
        fields = "__all__"


class JobDescriptionSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = JobDescription
        fields = "__all__"
