from django.db import models

# Create your models here.

class shortURL(models.Model):
    url = models.CharField(max_length = 220,)
    shortcode = models.CharField(max_length = 15, unique=True)

    def __str__(self):
        return str(self.url)



#***
#python manage.py makemigrations
#python manage.py migrate

#***