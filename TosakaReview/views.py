from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'TosakaReview/home.html', context)