from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'created_by', 'pub_date', 'edited_date' )
    exclude = ['postNumber', 'slug', 'created_by']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user

        super().save_model(request, obj, form, change)
