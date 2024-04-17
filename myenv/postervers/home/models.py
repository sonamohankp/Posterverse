from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Login_view(AbstractUser):
    is_users = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)


class users(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.CASCADE,related_name='users')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
class Designers(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.CASCADE, related_name='company')
    email = models.EmailField()
    contact_no = models.CharField(max_length=100)
    portfilo=models.CharField(max_length=100)
    status = models.BooleanField(default= False)

class DesignTask(models.Model):
    # Your existing fields
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    # New field for revision count
    revision_count = models.IntegerField(default=0)  # Initial revision count is 0

    def __str__(self):
        return self.title

class DesignSubmission(models.Model):
    task = models.ForeignKey(DesignTask, on_delete=models.CASCADE)
    designer = models.ForeignKey(Login_view, on_delete=models.CASCADE)
    design_draft = models.ImageField(upload_to='designs/')
    feedback = models.TextField(blank=True, null=True)
    revision_count = models.IntegerField(default=0)

class DesignRequest(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='design_requests/')
    payment_status = models.BooleanField(default=False)
    # Add more fields as needed
class Poster(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='posters/')
    # price = models.DecimalField(max_digits=10, decimal_places=2)

# class Cart(models.Model):
#     user = models.OneToOneField(Login_view, on_delete=models.CASCADE)
#     posters = models.ManyToManyField('Poster', related_name='carts')
