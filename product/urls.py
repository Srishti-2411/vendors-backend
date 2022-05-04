from django.urls import path

from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('Product-list/', views.taskList, name="Product-list"),
	path('Product-detail/<str:pk>/', views.taskDetail, name="Product-detail"),
	path('Product-create/', views.taskCreate, name="Product-create"),

	path('Product-update/<str:pk>/', views.taskUpdate, name="Product-update"),
	path('Product-delete/<str:pk>/', views.taskDelete, name="Product-delete"),
]