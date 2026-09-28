from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from .models import Task, SubTask, Note, Category, Priority
from .forms import TaskForm, SubTaskForm, NoteForm, CategoryForm, PriorityForm


class HomePageView(TemplateView):
    template_name = "home.html"


# =========================
# TASK VIEWS
# =========================

class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task-list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task-list")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("task-list")


# =========================
# SUBTASK VIEWS
# =========================

class SubTaskListView(ListView):
    model = SubTask
    template_name = "subtasks/subtask_list.html"
    context_object_name = "subtasks"


class SubTaskCreateView(CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = "subtasks/subtask_form.html"
    success_url = reverse_lazy("subtask-list")


class SubTaskUpdateView(UpdateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = "subtasks/subtask_form.html"
    success_url = reverse_lazy("subtask-list")


class SubTaskDeleteView(DeleteView):
    model = SubTask
    template_name = "subtasks/subtask_confirm_delete.html"
    success_url = reverse_lazy("subtask-list")


# =========================
# NOTE VIEWS
# =========================

class NoteListView(ListView):
    model = Note
    template_name = "notes/note_list.html"
    context_object_name = "notes"


class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/note_form.html"
    success_url = reverse_lazy("note-list")


class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/note_form.html"
    success_url = reverse_lazy("note-list")


class NoteDeleteView(DeleteView):
    model = Note
    template_name = "notes/note_confirm_delete.html"
    success_url = reverse_lazy("note-list")


# CATEGORY
class CategoryListView(ListView):
    model = Category
    template_name = "categories/category_list.html"
    context_object_name = "categories"


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "categories/category_form.html"
    success_url = reverse_lazy("category-list")


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "categories/category_form.html"
    success_url = reverse_lazy("category-list")


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "categories/category_confirm_delete.html"
    success_url = reverse_lazy("category-list")


# PRIORITY
class PriorityListView(ListView):
    model = Priority
    template_name = "priorities/priority_list.html"
    context_object_name = "priorities"


class PriorityCreateView(CreateView):
    model = Priority
    form_class = PriorityForm
    template_name = "priorities/priority_form.html"
    success_url = reverse_lazy("priority-list")


class PriorityUpdateView(UpdateView):
    model = Priority
    form_class = PriorityForm
    template_name = "priorities/priority_form.html"
    success_url = reverse_lazy("priority-list")


class PriorityDeleteView(DeleteView):
    model = Priority
    template_name = "priorities/priority_confirm_delete.html"
    success_url = reverse_lazy("priority-list")