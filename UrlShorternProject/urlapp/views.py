from django.shortcuts import render,redirect
from .models import UrlModel
import random

# Create your views here.
def urlindex(request):
    if request.method=='POST':
        link=request.POST.get('link')
        print(link)
        short_link=""
        alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
        url=UrlModel.objects.all()
        for i in url:
            if i.url_link==link:
                short_link=i.short_link
                break
        else:
            for i in range(1,7):
                letters=random.randint(1,len(alphabets)-1)
                let=alphabets[letters]
                short_link += let
            url=UrlModel(url_link=link,short_link=short_link)
            url.save()
        new_url="http://127.0.0.1:8000/" + short_link
        return render(request,"index.html",{"new_url":new_url})

    return render(request,"index.html")


def shortern(request,id):
    url=UrlModel.objects.filter(short_link=id)
    link=""
    for i in url:
        link=i.url_link
    return redirect(link)

    return None