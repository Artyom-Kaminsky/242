from django.contrib import admin

from posts.models import Posts, Images, Categories


@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    model = Posts
    list_display = (
        "title", "description", "date_publication", "user"
    )
    list_filter = ("title", "date_publication", "user")
    search_fields = ("title", "user")


@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    model = Images
    list_display = ("image", "post")
    list_filter = ("post",)
    search_fields = ("post",)


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    model = Categories
    # list_display = ("title", "post")
    search_fields = ("title",)
