from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import Organization, UserOrganizationRole
from .serializers import OrganizationSerializer, UserSerializer, UserOrganizationRoleSerializer

from rest_framework.permissions import IsAuthenticated
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'username': user.username}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_detail(request):
    user = request.user  # Get the authenticated user
    serializer = UserSerializer(user)  # Serialize the user data
    return Response(serializer.data, status=status.HTTP_200_OK)


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]


class UserOrganizationRoleViewSet(viewsets.ModelViewSet):
    queryset = UserOrganizationRole.objects.all()
    serializer_class = UserOrganizationRoleSerializer
    permission_classes = [IsAuthenticated]