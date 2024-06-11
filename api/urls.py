from django.urls import path
from .views import BookListCreateAPIView,BookRetriveAPIView,CategoryListCreateAPIView,CategoryRetriveAPIView, ClintListCreateAPIView,ClintRetriveAPIView


urlpatterns = [
    path('book/', BookListCreateAPIView.as_view()),
    path('book/<int:pk>/',BookRetriveAPIView.as_view()),
    path('category/',CategoryListCreateAPIView.as_view()),
    path('category/<int:pk>/',CategoryRetriveAPIView.as_view()),
    path('clint/',ClintListCreateAPIView.as_view()),
    path('clint/<int:pk>/',ClintRetriveAPIView.as_view()),
]
