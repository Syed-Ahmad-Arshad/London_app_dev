from rest_framework.views import APIView
from rest_framework.response import  Response



class HelloAPIView(APIView):
    """ Test API View """
    def get(self, request, format = None):
        """ Returns a list of of APIView features"""
        an_apiview = [
            'Uses HTTP methos as function  (get, post, patch, put , delete)',
            'Is similar to a Django traditional logic)',
            'Gives you the most control over your application logic)', 
            'Is mapped manually  to URLs)',
        ]
        return Response({'message':"Hello", 'an_apiview':an_apiview})

