from django.contrib import admin
from django.urls import path

from hangarin.views import (
    HomePageView,
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", HomePageView.as_view(), name="home"),

    path("tasks/", TaskListView.as_view(), name="task-list"),

    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create",
    ),

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
]