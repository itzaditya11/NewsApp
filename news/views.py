from django.shortcuts import render


# Create your views here.
def home(request):
    import requests
    import json
    news_api_request=requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=165edd88e50b4abc8de55459feed1255")
    api=json.loads(news_api_request.content) 
    return render(request,"home.html",{"api":api} )