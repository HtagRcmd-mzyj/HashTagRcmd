from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import EffmodelList
from .views import SaveImageList
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('image_model/', EffmodelList.as_view()),
    path('image_model/saveimg/', SaveImageList.as_view(), name= '_list')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)
