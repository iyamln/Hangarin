from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from hangarin.models import Task, Note, SubTask, Category, Priority


class Command(BaseCommand):
    help = "Create initial fake data for Hangarin"

    def handle(self, *args, **kwargs):
        self.create_tasks(20)
        self.create_notes(30)
        self.create_subtasks(40)

        self.stdout.write(
            self.style.SUCCESS(
                "Initial Hangarin data created successfully."
            )
        )

    def create_tasks(self, count):
        fake = Faker()

        categories = list(Category.objects.all())
        priorities = list(Priority.objects.all())

        if not categories or not priorities:
            self.stdout.write(
                self.style.ERROR(
                    "Please create Category and Priority records first."
                )
            )
            return

        for _ in range(count):
            Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                deadline=timezone.make_aware(
                    fake.date_time_this_month()
                ),
                status=fake.random_element(
                    elements=[
                        "Pending",
                        "In Progress",
                        "Completed",
                    ]
                ),
                category=fake.random_element(elements=categories),
                priority=fake.random_element(elements=priorities),
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"{count} tasks created successfully."
            )
        )

    def create_notes(self, count):
        fake = Faker()

        tasks = list(Task.objects.all())

        if not tasks:
            self.stdout.write(
                self.style.ERROR(
                    "Please create Task records first."
                )
            )
            return

        for _ in range(count):
            Note.objects.create(
                task=fake.random_element(elements=tasks),
                content=fake.paragraph(nb_sentences=3),
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"{count} notes created successfully."
            )
        )

    def create_subtasks(self, count):
        fake = Faker()

        tasks = list(Task.objects.all())

        if not tasks:
            self.stdout.write(
                self.style.ERROR(
                    "Please create Task records first."
                )
            )
            return

        for _ in range(count):
            SubTask.objects.create(
                parent_task=fake.random_element(elements=tasks),
                title=fake.sentence(nb_words=5),
                status=fake.random_element(
                    elements=[
                        "Pending",
                        "In Progress",
                        "Completed",
                    ]
                ),
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"{count} subtasks created successfully."
            )
        )