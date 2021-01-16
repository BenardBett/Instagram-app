from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.model):
      """
    Profile model

    Proxy Model that extends the base data with other information.
    """
    # Relation con la tabla user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    website= models.URLField(max_length=200, blank=True)
    biography= models.TextField(blank=True)
    phone_number= models.CharField(max_length=20, blank=True)
    
    
    
    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )