from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers, models, permission
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            "Uses Http method as functions (get, post, patch, put, delete)",
            "Is similar to traditional django view",
            "Gives you the most control over your application logic",
            "Is mapped manually to URLs"
        ]

        return Response({"message":"Hello World!","an_apiview":an_apiview})
    
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})
    

class HelloViewSet(viewsets.ViewSet):
    "Test API ViewSet"
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        "return a hellow message"
        a_viewset = [
            "Uses actions (list, create, retrieve, updata, partial_update",
            "autmatically maps to URLs using Routers"
            "Provides more functionality with less code"
        ]

        return Response({"message":"Hello", "a_viewset":a_viewset})

    def create(self,request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hi {name}!"
            return Response({"message":message})
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({"http_method": "GET"})
    
    def update(self, request, pk=None):
        """Handle updating part of an ojbect"""

        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """Handle partial updating part of an object"""

        return Response({"http_method": "PATCH"})

    def destroy(self, request, pk=None):
        """Handle deleting an object"""

        return Response({"http_method":"DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permission.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ("name", "email",)

class UserLoginApiView(ObtainAuthToken):
    """handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, and updating profile feed items"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permission.UpdateOwnProfile,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
    

