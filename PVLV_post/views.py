from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import PostForm
from .models import PostGeneratorConfig


def post(request):
    context = {}
    return render(request, 'console/post.html', context)


@login_required
def post_update(request):
    # if this is a POST request we need to process the form data
    try:
        post_instance = PostGeneratorConfig.objects.get(owner=request.user, scope='post')
    except PostGeneratorConfig.DoesNotExist:
        post_instance = PostGeneratorConfig(owner=request.user, scope='post')

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST, files=request.FILES, instance=post_instance)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            messages.success(request, f'Update successful!')
            return redirect('post')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm(instance=post_instance)

    return render(request, 'console/post.html', {'form': form})
