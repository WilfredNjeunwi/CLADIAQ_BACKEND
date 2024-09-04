from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import register, login, user_detail, OrganizationViewSet, UserOrganizationRoleViewSet

router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet)
# router.register(r'users', UserViewSet)
router.register(r'user-roles', UserOrganizationRoleViewSet)


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('me/', user_detail, name='user_detail'),
]