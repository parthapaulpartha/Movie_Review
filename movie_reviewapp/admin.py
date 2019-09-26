from django.contrib import admin
from .models import slider_images, movie_reviews, comment_movie_review, contact

# Register your models here.
# ------ For header --------
admin.site.site_header = 'Movie Review'

admin.site.register(slider_images)
admin.site.register(contact)

class MovieReviewAdmin(admin.ModelAdmin):
    list_display = 'movie_name', 'movie_release_date', 'movie_type', 'movie_director', 'movie_rating',
    list_filter = 'movie_name', 'movie_type', 'movie_director', 'movie_rating', 'movie_cast',
    search_fields = 'movie_name', 'movie_type',
admin.site.register(movie_reviews, MovieReviewAdmin)

class CommentMovieReviewAdmin(admin.ModelAdmin):
    list_display = 'name', 'post', 'rating', 'timestamp',
    list_filter = 'name', 'post', 'rating', 'timestamp',
    search_fields = 'name',
admin.site.register(comment_movie_review, CommentMovieReviewAdmin)
