from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:dept_code>/', views.classInDept, name='classInDept'),
    
]

