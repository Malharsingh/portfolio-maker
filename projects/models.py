from django.db import models

# Create your models here.
class Projects(models.Model):
    #Here will be included Image 
    image = models.ImageField(upload_to='images/')
    
    #here there will be the summary
    summary = models.CharField(max_length = 200)

