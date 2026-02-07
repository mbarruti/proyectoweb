from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # list_display = ('title', 'author', 'published')
    # ordering = ('author', 'created')
    # search_fields = ('title','content','author__username',
    #     'categories__name')
    # date_hierarchy = 'published'
    # list_filter = ('author__username','categories__name')

admin.site.register(Project, ProjectAdmin)