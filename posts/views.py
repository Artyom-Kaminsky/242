import logging
from typing import Literal

from django.views import View
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from posts.models import Posts, Images, Categories


logger = logging.getLogger()


class BasePostView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        is_active = request.user.is_active
        posts: QuerySet[Posts] = Posts.objects.all()
        return render(
            request=request, template_name="posts.html", 
            context={
                "posts": posts,
                "user": is_active
            }
        )


class PostsView(View):
    """Posts controller with all methods."""

    def get(self, request: HttpRequest) -> HttpResponse:
        is_active = request.user.is_active
        categories = Categories.objects.all()
        if not categories:
            return HttpResponse(
                content="<h1>Something went wrong</h1>"
            )
        if not is_active:
            return redirect(to="login")
        return render(
            request=request, template_name="post_form.html",
            context={"categories": categories}
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        images = request.FILES.getlist("images")
        post = Posts.objects.create(
            user=request.user,
            title=request.POST.get("title"),
            description=request.POST.get("description")
        )
        post.categories.set(request.POST.getlist("categories"))
        imgs = [Images(image=img, post=post) for img in images]
        Images.objects.bulk_create(imgs)
        # for img in images:
        #     Images.objects.create(
        #         image=img,
        #         post=post
        #     )
        return redirect(to="base")


class ShowDeletePostView(LoginRequiredMixin, View):
    login_url = "login"
    
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        try:
            post = Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            post = None
        author = False
        if request.user == post.user:
            author = True
        return render(
            request=request, template_name="pk_post.html",
            context={
                "post": post,
                "author": author
            }
        )

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        try:
            post = Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            pass
        if request.user != post.user:
            return HttpResponse(
                "<h1>У тебя здесь нет власти</h1>"
            )
        post.delete()
        return redirect(to="base")


class LikesView(LoginRequiredMixin, View):
    login_url = "login"

    def post(
        self, request: HttpRequest, 
        pk: int, action: Literal["like", "dislike"]
    ):
        try:
            post = Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            return
        result = {}
        if action == "like":
            post.likes += 1
            result["likes"] = post.likes
        elif action == "dislike":
            post.dislikes += 1
            result["dislikes"] = post.dislikes
        post.save(update_fields=["likes", "dislikes"])
        return JsonResponse(data=result)
