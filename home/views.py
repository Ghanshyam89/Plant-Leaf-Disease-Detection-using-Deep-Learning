from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable":"this is sent"
    }
    return render(request, 'index.html',context)
    # return HttpResponse("This is homepage")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is aboutpage")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is services page")

def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("This is contact page")