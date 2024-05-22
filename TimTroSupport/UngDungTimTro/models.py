from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    class UserRole(models.TextChoices):
        Admin = 'admin'
        Landlord = 'landlord'
        Tenant = 'tenant'

    role = models.CharField(max_length=10, choices= UserRole,default=UserRole.Tenant)
    email = models.EmailField(("email address"), blank=False, null=False)
    id_user = models.IntegerField(unique=False, blank=True, null=True)
    birth_date = models.DateField(null=True)
    address = models.CharField(max_length=128, null=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self._state.adding and self.id_user is None:
            count = User.objects.filter(role=self.role).count()
            self.id_user = count + 1
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Facility(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Property(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='product_images', null=False, default=None)
    # facilities = models.ManyToManyField(Facility)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}, {self.description}, {self.price}, {self.category}, {self.images}"

class Review(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.property.title}"


class Image(models.Model):
    product = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='product_images')
    image_url = models.URLField()
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.Property.title}"

class Comment(models.Model):
    product = models.ForeignKey(Property, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text  = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

