from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class HelloAPIView(APIView):
    """Test API View class"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format = None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Test Value 1',
            'Test Value 2',
        ]

        return Response({'message' : 'Hello User', 'an_apiview' : an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})

        else:
            return Response(serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk = None):
        """Handle updating request"""
        return Response({'method' : 'PUT'})

    def patch(self, request, pk = None):
        """Handle updating request"""
        return Response({'method' : 'PATCH'})

    def delete(self, request, pk = None):
        """Handle deleting request"""
        return Response({'method' : 'DELETE'})

class HelloViewSets(viewsets.ViewSet):
    """Test API Viewsets"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Returna hello request"""
        Test_Response = [
            'This is a List Viewset'
        ]

        return Response({'message':'HelloListView', 'viewsetResponse' : Test_Response})

    def create(self, request):
        """Create request"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self, request, pk = None):
        return Response({'message' : 'PUT'})

    def update(self, request, pk = None):
        return Response({'message' : 'UPDATE'})

    def partial_update(self, request, pk = None):
        return Response({'message' : 'PARTIAL_UPDATE'})

    def destroy(self, request, pk = None):
        return Response({'message' : 'DELETE'})

class UserProfileViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
