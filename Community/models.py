from django.db import models
from django.db.models import Model

# Create your models here.
class Member(Model):
    email_id=models.EmailField(max_length=245)



    