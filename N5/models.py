from django.db import models

# Create your models here.
from django.db import models


from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
# Create your models here.

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=False, null=False, )
    bio=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self,*args,**kwargs):
        if not self.slug:

            slug=slugify(f"{self.first_name}--(self.last_name)")
            self.slug=slug

            super().save(*args,**kwargs)


    def __str__(self):
        return self.username   