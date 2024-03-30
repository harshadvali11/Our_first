from django.shortcuts import render

# Create your views here.


def biriyani(request):
    return render(request,'biriyani.html')

def haleem(request):
    return render(request,'haleem.html')