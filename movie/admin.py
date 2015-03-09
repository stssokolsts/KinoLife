from django.contrib import admin
from models import MovieBase

class MoviesAdmin(admin.ModelAdmin):
    # sets values for how the admin site lists your products
    list_display = ('title_russian', 'year', 'url', 'rating_k', 'votes_k',)
    #list_display_links = ('name',)
    list_per_page = 50
    #ordering = ['-created_at']
    search_fields = ['title_russian',]
    #exclude = ('created_at', 'updated_at',)
    # sets up slug to be generated from product name
    #prepopulated_fields = {'slug': ('name',)}


admin.site.register(MovieBase, MoviesAdmin)
# Register your models here.
