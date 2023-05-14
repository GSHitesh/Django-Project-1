from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context = {
        "variable" : "This is an index page"
    }
    return render(request,'index.html', context)

def about(request):
    # return HttpResponse("This is the about page")
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')
