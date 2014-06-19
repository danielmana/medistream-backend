from django.conf.urls import patterns, url
from rest_framework.routers import DefaultRouter
from medistream import views


urlpatterns = patterns('',
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^users/register', 'medistream.views.register')
)

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'talks', views.TalkViewSet)
router.register(r'organizers', views.OrganizerViewSet)
router.register(r'speakers', views.SpeakerViewSet)
urlpatterns += router.urls