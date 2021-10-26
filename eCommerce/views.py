from django.shortcuts import render

# create homepage
def home(request):
    return render(request, 'home.html')