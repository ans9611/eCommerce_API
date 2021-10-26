from django.http import HttpResponse

# create homepage
def home(request):
    return HttpResponse('Homepage')