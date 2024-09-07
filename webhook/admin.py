from django.contrib import admin
import csv
from django.http import HttpResponse
from .models import *
def export_selected_to_csv(modeladmin, request, queryset):
    # Define HTTP response with CSV header
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="spotify_links.csv"'

    writer = csv.writer(response)
    
    # Write the header (field names)
    writer.writerow(['Title','category','url','Rating','Date_of_release','story','sent_at', 'is_sent','color'])

    # Write the data for the selected items
    for obj in queryset:
        writer.writerow([obj.Title, obj.url,obj.Rating,obj.story,obj.Date_of_release,obj.is_sent,obj.color, obj.sent_at])

    return response
def exportto_csv(modeladmin, request, queryset):
    # Define HTTP response with CSV header
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="spotify_links.csv"'

    writer = csv.writer(response)
    
    # Write the header (field names)
    writer.writerow(['discord_Bot','url',])

    # Write the data for the selected items
    for obj in queryset:
        writer.writerow([obj.name, obj.url,])

    return response
admin.site.register(SpotifyCategory)
@admin.register(WebhookMessage)
class WebhookMessageAdmin(admin.ModelAdmin):
    list_display = ('discord', 'sent_at', 'is_sent')
    list_filter = ('discord','is_sent',)
    
    search_fields = ('content', 'webhook_url')
@admin.register(Discord)
class DiscordBotsAdmin(admin.ModelAdmin):
    list_display=('name',)
    list_filter=('name',)
    actions = [exportto_csv]
@admin.register(Movies)
class MovieAdmin(admin.ModelAdmin):
    actions = [export_selected_to_csv,]

admin.site.register(Spotify)
admin.site.register(Annoucements)
admin.site.register(MovieCategory)