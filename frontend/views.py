from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'frontend/index.html')

def contact(request):
    return render(request,'frontend/contact.html')
