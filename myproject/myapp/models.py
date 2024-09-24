from django.db import models

class MyObject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    release_date = models.DateField()
    video = models.FileField(upload_to='videos/', blank=True, null=True)

    def __str__(self):
        return self.title
