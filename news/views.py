from django.shortcuts import render
import requests

# Create your views here.

def news(request):
  url = "https://newsapi.org/v2/top-headlines?country=kr&category=technology&apiKey=e9c1bb99094442d5945627242ac273f6"

  tech_news = requests.get(url).json()
  a = tech_news['articles']
  desc = []
  title = []
  img = []

  for i in range(len(a)):
    f = a[i]
    title.append(f['title'])
    desc.append(f['description'])
    img.append(f['urlToImage'])

  mylist = zip(title, desc, img)
  context = {'mylist' : mylist }

  return render(request, 'news/news.html', context)