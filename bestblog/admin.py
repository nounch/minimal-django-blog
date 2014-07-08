from bestblog.models import Post
from bestblog.models import User
from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    # fields = ['date', 'heading', 'description', 'text']
    fieldsets = [
        ('Header', {'fields': ['heading', 'date', 'description', 'publisher']}),
        ('Text', {'fields': ['text'], 'classes': ['collapse']}),
        ]
    list_display = ('heading', 'description', 'date')
    list_filter = ['date']
    search_fields = ['heading', 'description']
    date_hierarchy = 'date'


admin.site.register(Post, PostAdmin)

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['first_name', 'last_name', 'nick_name']}),
        ('Diverse', {'fields': ['email', 'joining_date'],
                     'classes': ['collapse']}),
        ]
    list_display = ('first_name', 'last_name', 'nick_name')

admin.site.register(User, UserAdmin)


