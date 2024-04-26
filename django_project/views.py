# views.py
from django.shortcuts import render
import requests
from django.shortcuts import render
from newsapi import NewsApiClient

def index(request):
    # Initialize NewsApiClient with your API key
    newsapi = NewsApiClient(

    api_key='42c6eaee15e644f0879f7f1274b479c2')# Fetch top headlines
    top_headlines = newsapi.get_top_headlines(language='en', page_size=5)

    # Extract relevant news data
    latest_news = []
    for article in top_headlines['articles']:
        headline = article['title']
        description = article['description']
        source = article['source']['name']
        url = article['url']  # Get the URL of the article
        latest_news.append({'headline': headline, 'source': source, 'url': url, 'description': description})

    # Prepare context data
    context = {
        'title': 'Welcome to News Portal',
        'latest_news': latest_news
    }

    # Render the template with context data
    return render(request, 'index.html', context)
def dogs(request):
  r1 = requests.get('https://api.github.com/events')
  data = r1.json()
  events = data[0]['repo']

  r2 = requests.get('https://www.boredapi.com/api/activity')
  data = r2.json()
  activity  = data['activity']

  r3 = requests.get('https://dog.ceo/api/breeds/image/random')
  res3 = r3.json()
  dog = res3['message']

  return render(request, 'templates/dogs.html', {'events': events, 'activity': activity, 'dog': dog})