from django.conf.urls import url
import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = (
    url(r'^upload/$', views.ImageUpload.as_view()),
    url(r'^upload_thumbnail$', views.ThumbnailUpload.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
