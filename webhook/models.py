
# Create your models here.
from django.db import models

class Fields (models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
class Discord(models.Model):
    name = models.CharField(max_length=2000)
    url = models.URLField(  )
    def __str__(self):
        return self.name
class SpotifyCategory(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Spotify'
        verbose_name_plural = 'Spotify Categories'
class MovieCategory(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Movie Category'
        verbose_name_plural = 'Movie Categories'
class WebhookMessage(models.Model):
    discord = models.ForeignKey(Discord, on_delete=models.CASCADE, null=False)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_sent = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Simple Webhook'
        verbose_name_plural = 'Simple Webhooks'
    def __str__(self):
        return f"Message {self.id} - {'Sent' if self.is_sent else 'Pending'}"
class Movies(models.Model):
    Discord__name="2"
    discord = models.ForeignKey(Discord,default=Discord__name, on_delete=models.CASCADE, null=False)
    Title = models.CharField(max_length=200)
    category = models.ForeignKey(MovieCategory,models.CASCADE)
    url = models.URLField()
    Rating = models.FloatField(default=0)
    Date_of_release = models.CharField(max_length=20)
    story = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_sent = models.BooleanField(default=False)
    color = models.CharField(max_length=12)
    def __str__(self):
        return f" {self.Title} - {'Sent' if self.is_sent else 'Pending'}"
    class Meta:
        verbose_name_plural = 'Movies and TV Series'
        verbose_name = 'Movie or TV Serie'
class Spotify(models.Model):
    discord = models.ForeignKey(Discord, on_delete=models.CASCADE, null=False)
    Title = models.CharField(max_length=200)
    category = models.ForeignKey(SpotifyCategory,models.CASCADE)
    url = models.URLField()
    Creator = models.CharField(max_length=200,verbose_name="Artist")
    color = models.CharField(max_length=12)

    sent_at = models.DateTimeField(auto_now_add=True)
    is_sent = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Spotify'
        verbose_name_plural = 'Spotify Playlist or Songs'
    def __str__(self):
        return f"{self.Title} By {self.Creator} - {'Sent' if self.is_sent else 'Pending'}"
class Annoucements(models.Model):
    discord = models.ForeignKey(Discord,models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(blank=True,null=True)
    color = models.CharField(max_length=12)
    sent_at = models.DateTimeField(auto_now_add=True)
    is_sent = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Annoucement'
        verbose_name_plural = 'Annoucements '
    def __str__(self):
        return f"{self.title}  - {'Sent' if self.is_sent else 'Pending'}"