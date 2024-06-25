from django.db import models
from django.contrib.auth.models import User

class Form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    form_id = models.CharField(max_length=100, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.form_id