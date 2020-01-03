from django.conf import settings
from django.db import models

# Create your models here.

from .utils import code_generator, create_shortcode

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class shortURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(shortURLManager,self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=100):
        print(items)
        qs = shortURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.id)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)

class shortURL(models.Model):
    url = models.CharField(max_length = 220,)
    shortcode = models.CharField(max_length = SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    #empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)

    objects = shortURLManager()
    #some_random = shortURLManager()
    
    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(shortURL, self).save(*args, **kwargs)


    # class Meta: 
    #     ordering = '-id'
    # def my_save(self):
    #     self.save()
    
    def __str__(self):
        return str(self.url)



#***
#python manage.py makemigrations
#python manage.py migrate

#***