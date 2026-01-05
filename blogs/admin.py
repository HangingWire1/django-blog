from django.contrib import admin
from blogs.models import Category, Blog, AboutUs, FollowUs


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title","category_id","category","author","status","is_featured")
    search_fields = ("id","title","category__category_name","status")
    list_editable = ("is_featured",)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name","pk",)

class AboutUsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = AboutUs.objects.all().count()
        if count == 0:
            return True
        return False

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(FollowUs)