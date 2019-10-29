import random
import string
from django.db import models

# Create your models here.

def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    # new_code = ''
    # for _ in range(size):
    #     new_code += random.choice(chars)
    # return new_code


    return ''.join(random.choice(chars) for _ in range(size))


class shortURL(models.Model):
    url = models.CharField(max_length = 220,)
    shortcode = models.CharField(max_length = 15, unique=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    #empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    def save(self, *args, **kwargs):
        print ("something")
        self.shortcode = code_generator()
        super(shortURL, self).save(*args, **kwargs)

    # def my_save(self):
    #     self.save()
    
    def __str__(self):
        return str(self.url)



#***
#python manage.py makemigrations
#python manage.py migrate

#***