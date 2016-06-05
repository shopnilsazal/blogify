from django.contrib import admin
from .models import Post, Category, Tag

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "post_categories", "post_tags", "updated")
    list_filter = ("categories", "updated")
    list_display_links = ("title", "post_categories", "post_tags", "updated")
    search_fields = ("title", "category", "tag")

    def post_categories(self, obj):
        return obj.list_categories()

    def post_tags(self, obj):
        return obj.list_tags()

    post_categories.short_description = "Categories"
    post_tags.short_description = "Tags"


admin.site.register(Category)
admin.site.register(Tag)
