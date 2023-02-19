from django.shortcuts import render

# Create your views here.
def bz(request):
    return render(request, 'База-знаний.html')

