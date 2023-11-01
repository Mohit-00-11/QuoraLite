# Generated by Django 4.2.7 on 2023-11-01 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Question",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("author", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="author_question", to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="Answer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("question", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="answers_to_question", to="app.question")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="user_answer", to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="Vote",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("answer", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="user_like", to="app.answer")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="user_vote", to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "unique_together": {("user", "answer")},
            },
        ),
    ]