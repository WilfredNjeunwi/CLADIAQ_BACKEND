from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, UserDetailView, OrganizationViewSet, UserOrganizationRoleViewSet

router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet)
router.register(r'user-roles', UserOrganizationRoleViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user-detail/', UserDetailView.as_view(), name='user-detail'),
    path('', include(router.urls)),  # Include the router URLs for organizations and user roles
]