from django.shortcuts import render

def main(request):
    return render(request, 'home.html')

def ways(request):
    return render(request, 'ways.html')