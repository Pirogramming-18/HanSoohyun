from django.urls import path
from .views import *
urlpatterns = [
    path("", ReviewListView.as_view(), name='list'),
    path("add/", ReviewCreateView.as_view(), name='add'),
    path("detail/<int:pk>/", ReviewDetailView.as_view(), name='detail'),
    path("update/<int:pk>/", ReviewUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", ReviewDeleteView.as_view(), name='delete'),
    
]