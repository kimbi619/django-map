from django.shortcuts import render

# Create your views here.



def homeView(request):
    return render(request, template_name='index.html')


def map_view(request):
    return render(request, template_name='map.html')