from django.shortcuts import render


def post(request):

    context = {
        'spot': {
        }

    }
    return render(request, 'console/post.html', context)
