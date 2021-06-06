from django.urls import path
from main import views

urlpatterns = [
    path('accueil/', views.homepage, name='accueil'),
    path("questionnaire", views.request_question, name='request_question'),
    path('conseil', views.denoument, name='denoument'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('register/', views.registerpage, name='register'),
]