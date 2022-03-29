from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'created_by', 'pub_date', 'edited_date' )
    exclude = ['postNumber', 'slug', 'created_by']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user

        super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)
