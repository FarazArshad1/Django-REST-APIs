from rest_framework import serializers
from ..models import Carlist, Showroomlist


class ShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroomlist
        fields = "__all__"


class Carserializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()
    class Meta:
        model = Carlist
        fields = "__all__" # -> This will include all the fields
        # But if want to include only specific fields then you can explicitly mention them
        # fields = ["name","description","active"]
        # If you want to inlcude all the fields except few then instead of mentioning all the fields you can use "exclude" 
        # exclude = ['name'] # -> This will include all the fields except name 
    def get_discounted_price(self,object):
        discountprice = object.price - 5000
        return discountprice


    def validate_price(self,value):
        if value <= 20000.00:
            raise serializers.ValidationError('Price must be Higher then 20000.00')
        return value


    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and description must be different')
        return data
    
    
   