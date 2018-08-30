from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()

    return render(request,
                  "HelloDjangoApp/index.html",
                  {
                      'title': "Hello Django",
                      'message': "Hello Django!",
                      'content': " on " + now.strftime("%A, %d %B, %Y at %X")       
                  }
             )
    
def about(request):
    return render(
        request,
        "HelloDjangoApp/about.html",
        {
            'title' : "About HelloDjangoApp",
            'content' : "Example app page for Django."
        }
    )

    #html_content = "<html><head><title>Hello, Django</title></head><body><strong>Hello, Django!</strong> on "
    #html_content += now.strftime("%A, %d %B, %Y at %X")
    #html_content += "</body></html>"
    
    #return HttpResponse(html_content)