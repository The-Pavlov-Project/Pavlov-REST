from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from .forms import PostForm, GeneratorSettingsInlineFormSet, PlatformInlineFormSet
from .models import Post, GeneratorSetting


@login_required
def post_update(request):
    # if this is a POST request we need to process the form data
    try:
        post = Post.objects.get(user=request.user)
    except Post.DoesNotExist:
        post = Post(user=request.user)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST, request.FILES, instance=post, prefix='post')
        formset_settings = GeneratorSettingsInlineFormSet(request.POST, request.FILES, instance=post, prefix="settings")
        formset_platforms = PlatformInlineFormSet(request.POST, instance=post, prefix="platforms")
        # check whether it's valid:
        if form.is_valid() and formset_settings.is_valid() and formset_platforms.is_valid():
            form.save()
            formset_settings.save()
            formset_platforms.save()
            messages.success(request, 'Update successful!')
            return redirect('console-post')
        else:
            messages.success(request, 'There are some problems fix and submit again!')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm(instance=post)
        formset_settings = GeneratorSettingsInlineFormSet(instance=post, prefix="settings")
        formset_platforms = PlatformInlineFormSet(instance=post, prefix="platforms")

    return render(
        request,
        'console/post.html',
        {
            'form': form,
            'formset_settings': formset_settings,
            'formset_platforms': formset_platforms,
        }
    )
