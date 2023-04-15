from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import KeyBERTModelList, KeyBERTModelDetail

urlpatterns = [
    path('text_model/', KeyBERTModelList.as_view()),
    path('text_model/<int:pk>/', KeyBERTModelDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
