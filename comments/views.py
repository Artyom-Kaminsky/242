import logging
from typing import Literal

from django.views import View
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect

from comments.models import Comments
from posts.models import Posts
from clients.models import Client


logger = logging.getLogger()


class AddComment(View):
    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        client = request.user
        if not isinstance(client, Client):
            return JsonResponse(data={"error": "not authorized"})
        posts = Posts.objects.filter(id=pk)
        if not posts:
            return JsonResponse(
                data={"error": f"Post with id {pk} not found"}
            )
        comment = Comments(
            post=posts[0], user=client,
            text=request.POST.get("text")
        )
        comment.save()
        return redirect("pk_post", pk=pk)


class AddReply(View):
    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        client = request.user
        if not isinstance(client, Client):
            return JsonResponse(data={"error": "not authorized"})
        comments = Comments.objects.filter(id=pk)
        if not comments:
            return JsonResponse(
                data={"error": f"Comment with id {pk} not found"}
            )
        comment = Comments(
            post=comments[0].post,
            user=client,
            parent=comments[0],
            text=request.POST.get("text")
        )
        comment.save()
        return redirect("pk_post", pk=comments[0].post.pk)
    