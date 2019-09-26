from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime

# Create your models here.
# -------- slider image --------
class slider_images(models.Model):
    image = models.ImageField(upload_to='slider_images', default='')
    title = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Slider Image'

#-------- Movie Information ------
class movie_reviews(models.Model):
    movie_name = models.CharField(max_length=100, default='')
    movie_release_date = models.DateField(default='')
    movie_duration = models.CharField(max_length=100, default='')
    TYPE_CHOICES = (
        ('action', 'Action'),
        ('adventure', 'Adventure'),
        ('comedy', 'Comedy'),
        ('crime', 'Crime'),
        ('drama', 'Drama'),
        ('fantasy', 'Fantasy'),
        ('historical', 'Historical'),
        ('historical fiction', 'Historical fiction'),
        ('horror', 'Horror'),
        ('philosophical', 'Philosophical'),
        ('political', 'Political'),
        ('romance', 'Romance'),
        ('science fiction', 'Science fiction'),
        ('thriller', 'Thriller'),
        ('western', 'Western'),
    )
    movie_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    movie_director = models.CharField(max_length=100, default='')
    movie_cast = models.TextField(max_length=9000, default='')
    movie_rating = models.CharField(max_length=100, default='0/0')
    movie_story = models.TextField(max_length=90000, default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    movie_image = models.ImageField(upload_to='movie images', default='')

    def __str__(self):
        return self.movie_name

    class Meta:
        verbose_name_plural = 'Movie Review'

#-------- Comment Movie Review ----------
class comment_movie_review(models.Model):
    post = models.ForeignKey(movie_reviews, on_delete=models.CASCADE,)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.CharField(max_length=100, default='')
    comment_review = models.TextField(max_length=90000, default='')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Comment Movie Review'

#------- Contact us -------
class contact(models.Model):
    name = models.ForeignKey(User, default=None, null=False, on_delete='')
    email = models.EmailField(max_length=50, default='')
    message = models.TextField(max_length=200, default='')

    def __str__(self):
        return str(self.name)