from rest_framework import serializers
from app.models import Rating
from .universityclass_schema import UniversityClassSerializer


class RatingSerializer(serializers.ModelSerializer):
    universityclass = UniversityClassSerializer(read_only=True)
    class Meta:
        model = Rating
        fields = '__all__'

class PostRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class PutRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['uuid', 'score', 'feedback']


    

    

