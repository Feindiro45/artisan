from django.urls import path
from .views import*

urlpatterns = [
    path('admin/authentification', home, name='home'),
    path('logout', logOut, name='logout')
    
]
