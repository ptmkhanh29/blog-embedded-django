from django.contrib import admin
from .models import Post, Category

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
# Customizing how models are displayed
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

    def list_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])

    list_categories.short_description = 'Categories'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ['name']