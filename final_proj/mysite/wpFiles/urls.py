from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:dept_id>/', views.classInDept, name='classInDept'),
    path('<int:class_id>/uploads', views.uploads, name='uploads'),
    path('upload',views.uploadFile, name='uploadFile'),
	
]

