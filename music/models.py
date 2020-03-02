from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f"{self.name}"

class Songs(models.Model):
    # song title
    title = models.CharField(max_length=255, null=False)
    # name of artist or group/band
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
