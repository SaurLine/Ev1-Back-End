from django.shortcuts import render

# Create your views here.



def inicio(request):
    return render(request, "app1/inicio.html")


def v1(request):
    return render(request, "app1/v1.html")

def v2(request):
    return render(request, "app1/v2.html")
