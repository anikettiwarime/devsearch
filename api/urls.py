from django.urls import path
# Register your models here.
from . import views
urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('projects/', views.getProjects),
    path('projects/<str:pk>/', views.getProject),
]
