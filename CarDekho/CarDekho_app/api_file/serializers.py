from rest_framework import serializers
from ..models import Carlist, Showroomlist, Review

# class ShowroomSerializer(serializers.ModelSerializer):
#     Showrooms = Carserializer(many=True, read_only=True)
#     class Meta:
#         model = Showroomlist
#         fields = "__all__"



class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



class Carserializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()
    Reviews = ReviewSerializers(many = True,read_only=True)
    class Meta:
        model = Carlist
        fields = "__all__"

    def get_discounted_price(self, object):
        if object.price is not None:
            discountprice = object.price - 5000
            return discountprice
        return None  # or you can return 0 or some default value



    def validate_price(self,value):
        if value <= 20000.00:
            raise serializers.ValidationError('Price must be Higher then 20000.00')
        return value


    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and description must be different')
        return data
    
    


class ShowroomSerializer(serializers.ModelSerializer):
    # Showrooms = Carserializer(many=True, read_only=True)
    # Showrooms = serializers.StringRelatedField(many=True)
    # Showrooms = serializers.PrimaryKeyRelatedField(many=True,read_only = True)
    Showrooms = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name = 'car_detail'
    )

    class Meta:
        model = Showroomlist
        fields = "__all__"

