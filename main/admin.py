from django.contrib import admin
from .models import Cinema, Movie, Review, Genre


class ReviewInline(admin.StackedInline):
    model = Review
    extra = 1


class MovieAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]
    search_fields = ['title', 'description']
    list_display = 'title id'.split()
    list_editable = ''.split()
    list_filter = ' cinema genres'.split()


admin.site.register(Cinema)
admin.site.register(Review)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)

