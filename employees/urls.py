from django.conf.urls import url
import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = (
    url(r'^teams/(?P<team_pk>[0-9]+)/estimators/(?P<pk>[0-9]+)/$', views.EstimatorDetail.as_view()),
    url(r'^teams/(?P<team_pk>[0-9]+)/estimators/$', views.EstimatorList.as_view()),
    url(r'^foreman/$', views.ForemanList.as_view()),
    url(r'^foreman/(?P<pk>[0-9]+)/$', views.ForemanDetail.as_view()),
    url(r'^me$', views.Me.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
