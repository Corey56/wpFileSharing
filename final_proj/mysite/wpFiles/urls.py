from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:dept_id>/', views.classInDept, name='classInDept'),
    path('<int:class_id>/uploads', views.uploads, name='uploads'),
    path('upload',views.uploadFile, name='uploadFile'),
    path(r"^search/", include("watson.urls", namespace="watson")),
    path('search', views.search, name='search'),
    path('signup/', views.signup.as_view(), name='signup'),
    
	
]
