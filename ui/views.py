from django.shortcuts import render, redirect
from .models import ShortenedUrl
from django.http import HttpResponse
import string
import random

# Create your views here.
def home(request):
    shortenedUrls = ShortenedUrl.objects.all()

    return render(request, 'search.html', {'title': 'URL Shortener', 'headline': 'Shorten Your URL!!', 'shortenedUrls': shortenedUrls})


def shorten(request):

    if 'actual-url' in request.POST:
        while True :
            random_string = ''.join((random.choice(string.ascii_letters+string.digits) for x in range(7)))
            if not ShortenedUrl.objects.filter(shortened_string=random_string).exists():
                break
    
        actual_url = request.POST['actual-url']

        u = ShortenedUrl(original_url=actual_url, shortened_string=random_string)
        u.save()

        shortenedUrls = ShortenedUrl.objects.all()

        return render(request, 'search.html', {'title': 'URL Shortener', 'headline': 'Shorten Your URL!!', 'shortenedUrls': shortenedUrls, 'shortString': random_string})
    
    else:
        return redirect("/")

def resolve(request, short_string):
    
    u = ShortenedUrl.objects.filter(shortened_string=short_string)
    if u.exists() :
        actual_url = u[0].original_url
        return redirect(actual_url)
    else :
        shortenedUrls = ShortenedUrl.objects.all()
        return render(request, 'search.html', {'title': 'URL Shortener', 'headline': 'Shorten Your URL!!', 'shortenedUrls': shortenedUrls, 'shortStringError': short_string})
