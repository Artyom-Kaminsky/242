from django.db import models
from django.utils import timezone

from clients.models import Client
from posts.models import Posts


class Comments(models.Model):
    post = models.ForeignKey(
        to=Posts,
        on_delete=models.CASCADE,
        related_name="post_comments",
        verbose_name="статья",
    )
    user = models.ForeignKey(
        to=Client,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="client_comments",
        verbose_name="автор комментария",
    )
    parent = models.ForeignKey(
        to="self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="child_comments",
        verbose_name="родительский комментарий",
    )
    text = models.TextField(
        verbose_name="текст комментария",
        max_length=2000,
    )
    date_created = models.DateTimeField(
        verbose_name="дата создания",
        default=timezone.now,
    )
    likes = models.PositiveIntegerField(
        verbose_name="лайки",
        default=0,
    )
    dislikes = models.PositiveIntegerField(
        verbose_name="дизлайки",
        default=0,
    )

    class Meta:
        ordering = ("id",)
        verbose_name = "комментарий"
        verbose_name_plural = "комментарии"

    def __str__(self):
        return f"{self.user} | {self.text[:20]}..."
