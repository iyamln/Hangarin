from django.db.models import Q
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from .models import Task, SubTask, Note, Category, Priority
from .forms import (
    TaskForm,
    SubTaskForm,
    NoteForm,
    CategoryForm,
    PriorityForm,
)
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

# =========================
# DASHBOARD
# =========================

class HomePageView(LoginRequiredMixin, TemplateView):
    login_url = "/accounts/login/"
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["task_count"] = Task.objects.count()
        context["subtask_count"] = SubTask.objects.count()
        context["note_count"] = Note.objects.count()
        context["category_count"] = Category.objects.count()
        context["priority_count"] = Priority.objects.count()

        context["pending_count"] = Task.objects.filter(
            status="Pending"
        ).count()

        context["in_progress_count"] = Task.objects.filter(
            status="In Progress"
        ).count()

        context["completed_count"] = Task.objects.filter(
            status="Completed"
        ).count()

        context["recent_tasks"] = Task.objects.order_by(
            "-created_at"
        )[:5]

        return context

# =========================
# TASKS
# =========================

class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"
    paginate_by = 6

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.GET.get("q")

        if query:
            qs = qs.filter(
                Q(title__icontains=query)
                | Q(description__icontains=query)
                | Q(status__icontains=query)
            )

        return qs

    def get_ordering(self):
        allowed = ["title", "deadline", "status"]

        sort_by = self.request.GET.get("sort_by")

        if sort_by in allowed:
            return sort_by

        return "title"


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
# SUBTASKS
# =========================

class SubTaskListView(ListView):
    model = SubTask
    template_name = "subtasks/subtask_list.html"
    context_object_name = "subtasks"
    paginate_by = 6

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.GET.get("q")

        if query:
            qs = qs.filter(
                Q(title__icontains=query)
                | Q(status__icontains=query)
                | Q(parent_task__title__icontains=query)
            )

        return qs


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
# NOTES
# =========================

class NoteListView(ListView):
    model = Note
    template_name = "notes/note_list.html"
    context_object_name = "notes"
    paginate_by = 6

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.GET.get("q")

        if query:
            qs = qs.filter(
                Q(content__icontains=query)
                | Q(task__title__icontains=query)
            )

        return qs


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


# =========================
# CATEGORIES
# =========================

class CategoryListView(ListView):
    model = Category
    template_name = "categories/category_list.html"
    context_object_name = "categories"
    paginate_by = 6

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.GET.get("q")

        if query:
            qs = qs.filter(
                Q(name__icontains=query)
            )

        return qs


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


# =========================
# PRIORITIES
# =========================

class PriorityListView(ListView):
    model = Priority
    template_name = "priorities/priority_list.html"
    context_object_name = "priorities"
    paginate_by = 6

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.GET.get("q")

        if query:
            qs = qs.filter(
                Q(name__icontains=query)
            )

        return qs


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
    form_class = PriorityForm
    template_name = "priorities/priority_confirm_delete.html"
    success_url = reverse_lazy("priority-list")

def custom_logout(request):
    logout(request)
    return redirect("account_login")