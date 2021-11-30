from rest_framework import serializers

from .models import Car

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Car

        fields = ('id','name_of_car','created_at','user','body')