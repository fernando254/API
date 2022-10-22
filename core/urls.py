
from django.urls import path, include
from .views import home, UsuariViewSet, PersonaVievSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuarios', UsuariViewSet)
router.register(r'personas', PersonaVievSet)

urlpatterns = [
    
    path('', home, name="home"),
    path('api/', include(router.urls)),
    
]