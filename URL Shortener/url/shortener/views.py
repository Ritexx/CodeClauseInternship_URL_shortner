# shortener/views.py
from django.shortcuts import render, redirect
from .models import ShortenedURL
import string
import random

def generate_random_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        short_url = generate_random_short_url()
        shortened_url = ShortenedURL(original_url=original_url, short_url=short_url)
        shortened_url.save()
        return render(request, 'shortener/success.html', {'shortened_url': shortened_url})
    return render(request, 'shortener/index.html')


# shortener/views.py
from django.shortcuts import render, redirect
from .models import ShortenedURL

def generate_random_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        short_url = generate_random_short_url()
        shortened_url = ShortenedURL(original_url=original_url, short_url=short_url)
        shortened_url.save()
        return render(request, 'shortener/success.html', {'shortened_url': shortened_url})
    return render(request, 'shortener/index.html')

def redirect_to_original(request, short_url):
    shortened_url = ShortenedURL.objects.get(short_url=short_url)
    return redirect(shortened_url.original_url)

