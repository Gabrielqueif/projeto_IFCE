from django.shortcuts import render


def inicio(request):
    return render(
        request,
        'homepage/index.html'
    )


def memorial(request):
    return render(
        request,
        'homepage/memorial.html'
    )


def calculadora(request):
    return render(
        request,
        'homepage/calculadora.html'
    )
