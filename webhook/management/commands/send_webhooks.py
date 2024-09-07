import requests
from django.core.management.base import BaseCommand
from webhook.models import *

class Command(BaseCommand):
    help = 'Send webhook messages stored in the database'

    def handle(self, *args, **options):
        messages = WebhookMessage.objects.filter(is_sent=False)

        for message in messages:
            response = requests.post(message.discord.url, json={"content": message.content})
            if response.status_code == 204:
                message.is_sent = True
                message.save()
                self.stdout.write(self.style.SUCCESS(f"Sent message {message.id}"))
            else:
                self.stdout.write(self.style.ERROR(f"Failed to send message {message.id}"))
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
                self.stdout.write(self.style.SUCCESS(f"Sent message {message.id}"))
            else:
                self.stdout.write(self.style.ERROR(f"Failed to send message {message.id}"))
        spotifys = Spotify.objects.filter(is_sent=False)

        for message in spotifys:
            color_decimal = int(message.color.lstrip('#'), 16)
            data = {

            "embeds": [
            {
            "title":f"{message.Title}",
            "description": f"{message.category.name}",
            "color":  color_decimal,  # Optional: Color of the embed
            
            "fields":[
                {
                "name":"Artist",
                "value":f"{message.Creator}/ 10 by IMDB",
                "inline":False,
            },
                            
            {
                 "name":"Spotify",
                 "url":f"{message.url}",
                 "inline":True,
            }


            ],

            "footer": {"text":f"Added at {message.sent_at}"},

        }
    ]
}

            response = requests.post(message.discord.url, json=data)      
            if response.status_code == 204:
                message.is_sent = True
                message.save()
                self.stdout.write(self.style.SUCCESS(f"Sent message {message.id}"))
            else:
                self.stdout.write(self.style.ERROR(f"Failed to send message {message.id}"))
        