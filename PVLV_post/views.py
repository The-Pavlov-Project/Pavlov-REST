from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    UpdateView,
)

from .models import PostGeneratorConfig


def post(request):
    context = {}
    return render(request, 'console/post.html', context)


class PostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Update the post settings"""
    model = PostGeneratorConfig
    template_name = 'console/post.html'
    fields = ['name', 'post', 'spot']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        config = self.get_object()
        if self.request.user == config.author:
            return True
        return False
