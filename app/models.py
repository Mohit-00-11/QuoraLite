from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    content = models.TextField()
    author = models.ForeignKey(
        to=User, on_delete=models.CASCADE,
        related_name="author_question"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        def __str__(self) -> str:
            return self.title


class Answer(models.Model):
    content = models.TextField()
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE,
        related_name="user_answer"
    )
    question = models.ForeignKey(
        to=Question, on_delete=models.CASCADE,
        related_name="answers_to_question"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        def __str__(self) -> str:
            return self.question


class Vote(models.Model):
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE,
        related_name="user_vote"
    )
    answer = models.ForeignKey(
        to=Answer, on_delete=models.CASCADE,
        related_name="user_like"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["user", "answer"]

        def __str__(self) -> str:
            return self.user.first_name
