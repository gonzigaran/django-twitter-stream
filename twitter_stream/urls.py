from django.conf.urls import url
from twitter_stream import views

app_name = 'twitter_stream'
urlpatterns = [
    url(r'^$', views.status, name='status'),
    url(r'^update/', views.json_status, name='update'),
]