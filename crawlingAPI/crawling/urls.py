from . import views
from django.urls import path
from .views import CrawlingList, CrawlingDetail, SaveImgList2
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('crawling/', CrawlingList.as_view()),
    path('crawling/<int:pk>/', CrawlingDetail.as_view()),
    path('crawling/saveimg/', SaveImgList2.as_view()),
    #path('test/', ShowTopHashtag.as_view())
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
