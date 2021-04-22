from django.urls import path
from studentapp import views

urlpatterns = [  
    path('', views.student_show, name='student_show'),
    path('setcookie', views.setcookie),
    path('getcookie', views.showcookie),
    
    
]