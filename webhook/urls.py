from django.urls import path
from .views import *

urlpatterns = [
    path('', SendWebhookMessages.as_view(), name='send_webhooks'),
    path('Movies/', SendWebhookMovie.as_view(), name='send_webhooks'),
    path('Annoucements/', SendWebhookAnnoucements.as_view(), name='annoucements'),
    path('Spotify/', SendWebhookSpotify.as_view(), name='Spotufy'),

]
