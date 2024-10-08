from django.db import models

# Create your models here.
class Movie(models.Model):
    TYPE=[('movie','movie'),('Sport', 'Sport'),
        ('TV Show', 'TV Show'),
        ]
    title=models.CharField(max_length=1000)
    video_link=models.TextField()
    type=models.CharField(max_length=100, choices=TYPE)
    thumbnail=models.ImageField(upload_to='media/',blank=True)
    views=models.IntegerField(default=0)