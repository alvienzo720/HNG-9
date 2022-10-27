from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoints),
    
    path('interns', views.InternList.as_view()),

   

    
]