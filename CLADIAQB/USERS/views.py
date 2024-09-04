from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import UserSerializer, OrganizationSerializer, UserOrganizationRoleSerializer
from .models import CustomUser, Organization, UserOrganizationRole

class RegisterView(APIView):
    """
    Register a new user.
    """
    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={
            201: openapi.Response('User created', UserSerializer),
            400: openapi.Response('Invalid input')
        }
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'username': user.username, 'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    """
    Login an already existing user.
    """
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password')
            }
        ),
        responses={
            200: openapi.Response('Login Success', openapi.Schema(type=openapi.TYPE_OBJECT, properties={'token': openapi.Schema(type=openapi.TYPE_STRING)})),
            401: openapi.Response('Invalid credentials')
        }
    )
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={200: openapi.Response('User details', UserSerializer)}
    )
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Organization ViewSet
class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={200: OrganizationSerializer(many=True), 401: 'Unauthorized'}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

# User Organization Role ViewSet
class UserOrganizationRoleViewSet(viewsets.ModelViewSet):
    queryset = UserOrganizationRole.objects.all()
    serializer_class = UserOrganizationRoleSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={200: UserOrganizationRoleSerializer(many=True), 401: 'Unauthorized'}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)