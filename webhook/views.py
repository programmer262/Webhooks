import requests

from django.http import HttpResponse
from django.views import View
from django.shortcuts  import render
from .models import *

class SendWebhookMessages(View):
    
    def get(self, request, *args, **kwargs):
        # Fetch unsent messages
        messages = WebhookMessage.objects.filter(is_sent=False)

        for message in messages:
            data = {
        'content':'None '
}

            response = requests.post(message.discord.url, json=data)
            if response.status_code == 204:
                message.is_sent = True
                message.save()
        spotifys = WebhookMessage.objects.filter(is_sent=True,discord__name="Spotify Hook Cod Server")
        movies = WebhookMessage.objects.filter(is_sent=True,discord__name="Movies Cod Server")
        return render(request,'home.html',context={'messages':messages,'contents':spotifys,'movies':movies})
class SendWebhookMovie(View):
    
    def get(self, request, *args, **kwargs):
        movies = Movies.objects.filter(is_sent=False)

        for message in movies:
            color_decimal = int(message.color.lstrip('#'), 16)
            data = {

            "embeds": [
            {
            "title":f"{message.Title}",
            "description": f"{message.story}",
            "color":  color_decimal,  # Optional: Color of the embed
            "image": {
                "url": f"{message.url}"
            },
            "fields":[
                {
                "name":"Rating",
                "value":f"{message.Rating}/ 10 by IMDB",
                "inline":True,
            },
                           {
                "name":"Category",
                "value":f"{message.category}",
                "inline":True,
            },
                          
            {
                "name":"Date of release:",
                "value":f"{message.Date_of_release}",
                "inline":True,
            },

            ]
        }
    ]
}

        response = requests.post(message.discord.url, json=data)            
        if response.status_code == 204:
                message.is_sent = True
                message.save()

        return HttpResponse("<h1>Message Sent</h1>")

class SendWebhookSpotify(View):
    
    def get(self, request, *args, **kwargs):
        spotifys = Spotify.objects.filter(is_sent=False)

        for message in spotifys:
            color_decimal = int(message.color.lstrip('#'), 16)
            data = {

            "embeds": [
            {
            "title":f"{message.Title}",
            "description": f"{message.category.name}",
            "color":  color_decimal,  # Optional: Color of the embed
            "url":f"{message.url}",
            

            "fields":[
                {
                "name":"Artist",
                "value":f"{message.Creator}",
                "inline":False,
            },
                            


            ],

            "footer": {"text":f"Added at {message.sent_at}"},

        }
    ]
}

        response = requests.post(message.discord.url, json=data)            
        if response.status_code == 204:
                message.is_sent = True
                message.save()
                return HttpResponse("<h1>Message Sent</h1>")
        else:
             return HttpResponse('There been a problem')
class SendWebhookAnnoucements(View):
    
    def get(self, request, *args, **kwargs):
        spotifys = Annoucements.objects.filter(is_sent=False)

        for message in spotifys:
            color_decimal = int(message.color.lstrip('#'), 16)
            data = {

            "embeds": [
            {
            "title":f"{message.title}",
            "description": f"{message.description}",
            "color":  color_decimal,  # Optional: Color of the embed




            "footer": {"text":f"Added at {message.sent_at}"},

        }
    ]
}
            if message.url:
                data["embeds"][0]["url"] = message.url
        response = requests.post(message.discord.url, json=data)            
        if response.status_code == 204:
                message.is_sent = True
                message.save()
                return HttpResponse("<h1>Message Sent</h1>")
        else:
             return HttpResponse('There been a problem')
