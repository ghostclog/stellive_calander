from django.shortcuts import render

# Create your views here.
def main_page(request):
    if request.method == "GET":
        return render(request,"page.html")
    
def stella_page(request,stella):
    if request.method == "GET":
        return render(request,"members.html",{'stella':stella})