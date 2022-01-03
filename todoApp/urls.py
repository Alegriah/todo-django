from todoApp.views import index
from django.contrib import admin
from django.urls import path, include
from todo.views import (
    list_view as todo_list_view,
    delete_view as todo_delete_view,
    detail_view as todo_detail_view,
    category_view as todo_category_view
)
import debug_toolbar


urlpatterns = [
    path('', index, name="index"),
    path('del/<item_id>', todo_delete_view, name="del"),
    path('todo/admin/', admin.site.urls, name="admin"),
    path('__debug__/', include(debug_toolbar.urls)),
    path('todo/<int:pk>/', todo_detail_view, name="detail"),
    path('todo/<category>', todo_category_view, name="category"),
    path('todo/', todo_list_view, name="todo"),
]
