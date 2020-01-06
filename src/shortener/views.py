from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import shortURL
# Create your views here.

#function based view
def short_redirect_View(request, shortcode=None, *args, **kwargs):
    # obj = shortURL.objects.get(shortcode=shortcode)

    obj = get_object_or_404(shortURL, shortcode=shortcode)
    # obj_url = obj.url

    # try:
    #     obj = shortURL.objects.get(shortcode=shortcode)
    # except:
    #     obj = shortURL.objects.all().first()
    # obj_url = None
    # qs = shortURL.objects.filter(shortcode__iexact=shortcode.upper())
    # if qs.exists() and qs.count() == 1:
    #     obj = qs.first()
    return HttpResponse("hello {sc}".format(sc = obj.url))


#class based view
class shortCBView(View): 
    def get(self, request, shortcode=None, *args,**kwargs):
        obj = get_object_or_404(shortURL, shortcode=shortcode)
        return HttpResponse("hello again {sc}".format(sc=obj.url))

    def post(self, request, *args, **kwargs):
        return HttpResponse();
