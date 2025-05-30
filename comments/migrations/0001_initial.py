# Generated by Django 5.1.7 on 2025-04-28 12:24

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("posts", "0004_remove_categories_post_posts_categories"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Comments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "text",
                    models.TextField(max_length=2000, verbose_name="текст комментария"),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="дата создания"
                    ),
                ),
                ("likes", models.PositiveIntegerField(default=0, verbose_name="лайки")),
                (
                    "dislikes",
                    models.PositiveIntegerField(default=0, verbose_name="дизлайки"),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="child_comments",
                        to="comments.comments",
                        verbose_name="родительский комментарий",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_comments",
                        to="posts.posts",
                        verbose_name="статья",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="client_comments",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="автор комментария",
                    ),
                ),
            ],
            options={
                "verbose_name": "комментарий",
                "verbose_name_plural": "комментарии",
                "ordering": ("id",),
            },
        ),
    ]
