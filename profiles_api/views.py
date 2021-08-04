from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import status
from profiles_api import permissions, serializers
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions


class HelloAPIView(APIView):
    """ Test API View """
    serializer_class = serializers.HelloSerializer
    def get(self, request, format = None):
        """ Returns a list of of APIView features"""
        an_apiview = [
            'Uses HTTP methos as function  (get, post, patch, put , delete)',
            'Is similar to a Django traditional logic)',
            'Gives you the most control over your application logic)', 
            'Is mapped manually  to URLs)',
        ]
        return Response({'message':"Hello", 'an_apiview':an_apiview})

    def post(self, request,):
        """ Create a hello message with our name """
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello (name)'
            return Response({'message':message})
        else: 
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """ Handle updating an object """
        return Response({'method':'PUT'})

    
    def patch(self, request, pk = None):
        """ Handle partial update of an object """
        return Response({'method':'PATCH'})


    def delete(self, request, pk = None):
        """ Delete an object """
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """ Test API Viewset"""
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """ Returna a hello message"""
        a_viewset = [ 
            'Uses actions (list, create, retrieve, update, partial_update',
            'Autmoatically maps to URLs using Routers',
            'Provides more functioanlity with more code',

            ]
        return Response({'message':'Hello!', 'a_viewset':a_viewset})


    def create(self, request):
        """ Create a new hello message """
        serializer = self.serializer_class(data=request.data)


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all() 
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile,)
