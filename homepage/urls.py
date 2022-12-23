from django.urls import path
from .views import home, list_techniciens, blog, contact, don
from django.conf.urls import handler404

urlpatterns = [
    path('', home),
    path('liste/techniciens_par_catégories/', list_techniciens),
    path('blog/', blog, name="blog"),
    path('contact/', contact, name="contact"),
    path('faite un don/', don)
    
]

handler404 ="homepage.views.handel404"
