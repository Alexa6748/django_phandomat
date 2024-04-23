from django.shortcuts import render

def first_page(request):
    return render(request, './index.html')

# Create your views here.
def phandomat_page_open(request):
    return render(request, './phandomat_page.html')