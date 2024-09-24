from django.shortcuts import render
from .models import Carlist, Showroomlist, Review
from django.http import JsonResponse
from .api_file.serializers import Carserializer,ShowroomSerializer, ReviewSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers



"""  Concrete view classes in Django Rest Framework (DRF) are pre-built views
    that combine generic views and mixins to provide common, ready-to-use API
    behaviors for typical CRUD operations (Create, Read, Update, Delete).
    These views are called concrete because they represent specific
    implementations of common patterns, such as retrieving an object or listing objects,
    as opposed to the more abstract and customizable generic views.

    Concrete view classes simplify the process of building APIs by offering 
    out-of-the-box functionality without needing to mix and match 
    individual mixins or override methods. With these views, you only need
    to specify the queryset and serializer_class, and DRF takes care of the rest."""

# class ReviewDetail(mixins.RetrieveModelMixin,
#                    mixins.CreateModelMixin,
#                    generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializers

    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class ReviewList(mixins.ListModelMixin,
#                  mixins.CreateModelMixin,
#                  generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializers

#     authentication_classes = [SessionAuthentication]
#     permission_classes = [DjangoModelPermissions]

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

## ------------------------------------------------------------------------------------------------ ##

# from django.http import HttpResponse
# import json


# Create your views here.


# def car_list_view(request):
#     cars = Carlist.objects.all()
#     data = {
#         'cars' : list(cars.values()),
#     }
#     data_json = json.dumps(data)
#     return HttpResponse(data_json,content_type = 'application/json')



# def car_detail_view(request,pk):
#     car = Carlist.objects.get(pk=pk)
#     data = {
#         'name' : car.name,
#         'description' : car.description,
#         'active' : car.active
#     }
#     return JsonResponse(data)


@api_view(['GET','POST'])
def car_list_view(request):
    if request.method == 'GET':   
        car = Carlist.objects.all()
        serializer = Carserializer(car, many = True)
        return Response(serializer.data)
    

    if request.method == 'POST':
        serializer = Carserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def car_detail_view(request,pk):
    if request.method == 'GET':
        try:
            car = Carlist.objects.get(pk=pk)
        except:
            return Response({'Error' : 'Car Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = Carserializer(car)
        return Response(serializer.data)
    

    if request.method == 'PUT':
        car = Carlist.objects.get(pk=pk)
        serializer = Carserializer(car,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method =='DELETE':
        car = Carlist.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class Showroom_Viewset(viewsets.ModelViewSet):
    queryset = Showroomlist.objects.all()
    serializer_class = ShowroomSerializer



# class Showroom_Viewset(viewsets.ViewSet):

#     def list(self, request):
#         serializer_context = {
#             'request': request,
#         }
#         queryset = Showroomlist.objects.all()
#         serializer = ShowroomSerializer(queryset, many=True,context=serializer_context)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         serializer_context = {
#             'request': request,
#         }
#         queryset = Showroomlist.objects.all()
#         user = get_object_or_404(queryset, pk = pk)
#         serializer = ShowroomSerializer(user,context=serializer_context)
#         return Response(serializer.data)   

#     def create(self, request):
#         serializer_context = {
#             'request': request,
#         }
#         serializer = ShowroomSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,context=serializer_context)
#         else:
#             return Response(serializer.errors, context=serializer_context, status= status.HTTP_400_BAD_REQUEST)

class Showroom_View(APIView):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        showroom = Showroomlist.objects.all()
        serializer = ShowroomSerializer(showroom, many=True, context = {'request' : request})
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ShowroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class Showroom_Details(APIView):
    def get(self,request,pk):
        try:
            showroom = Showroomlist.objects.get(pk=pk)
        except Showroomlist.DoesNotExist:
            return Response({'Error' : 'Showroom Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        serializers = ShowroomSerializer(showroom)
        return Response(serializers.data)
    
    def put(self,request,pk):
        showroom = Showroomlist.objects.get(pk=pk)
        serializer = ShowroomSerializer(showroom,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
            
    def delete(self,request,pk):
        showroom = Showroomlist.objects.get(pk=pk)
        showroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  