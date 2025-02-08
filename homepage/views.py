from django.shortcuts import render


def lista(request):
    return render(
        request,
        'homepage/index.html'
    )
