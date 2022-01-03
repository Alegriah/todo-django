from django.contrib import admin
from .models import Todo, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


def mark_todo(modeladmin, request, queryset):
    for todo in queryset:
        todo.fait = True
        todo.save()
mark_todo.short_description = 'Marquer comme "fait"'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'detail', 'date', 'done')
    list_filter = ('title', 'category', 'date')
    search_fields = ['title', 'date']
    actions = [mark_todo, ]


admin.site.register(Todo, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
