from django.contrib import admin


class SearchTermAdmin(admin.ModelAdmin):
    list_display = ('__unicode__','ip_address', 'search_date')
    list_filter = ('ip_address', 'q')
# Register your models here.
