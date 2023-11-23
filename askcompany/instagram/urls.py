
from django.urls import path, include
from .import views
urlpatterns = [
    path("", views.post_list),
    path('<int:pk>/', views.post_detail)
]
