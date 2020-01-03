from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import shortURL
# Create your views here.

#function based view
def short_redirect_View(request, shortcode=None, *args, **kwargs):
    # print(request.user)
    # print(request.user.is_authenticated())
    # obj = shortURL.objects.get(shortcode=shortcode)
    # try:
    #     obj = shortURL.objects.get(shortcode=shortcode)
    # except:
    #     obj = shortURL.objects.all().first()
    obj_url = None
    qs = shortURL.objects.filter(shortcode__iexact=shortcode.upper())
    if qs.exists() and qs.count() == 1:
        obj = qs.first()
        obj_url = obj.url
    return HttpResponse("hello {sc}".format(sc = obj.url))


#class based view
class shortCBView(View): 
    def get(self, request, shortcode=None, *args,**kwargs):
        return HttpResponse("hello again {sc}".format(sc=shortcode))
