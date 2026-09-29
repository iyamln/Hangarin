from django.contrib import admin
from django.urls import path, include

from hangarin.views import (
    HomePageView,
    custom_logout,
    

    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,

    SubTaskListView,
    SubTaskCreateView,
    SubTaskUpdateView,
    SubTaskDeleteView,

    NoteListView,
    NoteCreateView,
    NoteUpdateView,
    NoteDeleteView,

    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,

    PriorityListView,
    PriorityCreateView,
    PriorityUpdateView,
    PriorityDeleteView,
)



urlpatterns = [
    path("admin/", admin.site.urls),

    

    path(
        "accounts/", 
        include("allauth.urls")),

    path(
        "logout/", 
        custom_logout, 
        name="custom-logout"),

    path("", HomePageView.as_view(), name="home"),

    # TASKS
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "tasks/<int:pk>/edit/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),

    # SUBTASKS
    path(
        "subtasks/",
        SubTaskListView.as_view(),
        name="subtask-list",
    ),
    path(
        "subtasks/create/",
        SubTaskCreateView.as_view(),
        name="subtask-create",
    ),
    path(
        "subtasks/<int:pk>/edit/",
        SubTaskUpdateView.as_view(),
        name="subtask-update",
    ),
    path(
        "subtasks/<int:pk>/delete/",
        SubTaskDeleteView.as_view(),
        name="subtask-delete",
    ),

    # NOTES
    path(
        "notes/",
        NoteListView.as_view(),
        name="note-list",
    ),
    path(
        "notes/create/",
        NoteCreateView.as_view(),
        name="note-create",
    ),
    path(
        "notes/<int:pk>/edit/",
        NoteUpdateView.as_view(),
        name="note-update",
    ),
    path(
        "notes/<int:pk>/delete/",
        NoteDeleteView.as_view(),
        name="note-delete",
    ),

    # CATEGORIES
    path(
        "categories/", 
        CategoryListView.as_view(), 
        name="category-list"),
    path(
        "categories/create/",
        CategoryCreateView.as_view(),
        name="category-create"),
    path(
        "categories/<int:pk>/edit/", 
        CategoryUpdateView.as_view(), 
        name="category-update"),
    path(
        "categories/<int:pk>/delete/", 
        CategoryDeleteView.as_view(), 
        name="category-delete"),

    # PRIORITIES
    path(
        "priorities/", 
        PriorityListView.as_view(), 
        name="priority-list"),
    path(
        "priorities/create/", 
        PriorityCreateView.as_view(), 
        name="priority-create"),
    path(
        "priorities/<int:pk>/edit/", 
        PriorityUpdateView.as_view(), 
        name="priority-update"),
    path(
        "priorities/<int:pk>/delete/", 
        PriorityDeleteView.as_view(), 
        name="priority-delete"),
    

]