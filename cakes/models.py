from django.db import models
from cloudinary.models import CloudinaryField


class CakeCategory(models.Model):

    category = models.CharField(max_length=100, default="to be set")

    def __str__(self):
        return str(self.category)


class CakeFlavour(models.Model):
    flavour = models.CharField(max_length=50)

    def __str__(self):

        return str(self.flavour)


class CakeColor(models.Model):
    color = models.CharField(max_length=50)

    def __str__(self):
        return str(self.color)


class IndividualCake(models.Model):
    description = models.TextField(default="")

    def __str__(self):
        return str(self.name)

    name = models.CharField(max_length=100)

    category = models.ForeignKey(
        CakeCategory,
        on_delete=models.PROTECT,
        default=None,
    )

    is_gluten_free = models.BooleanField()

    is_plant_based = models.BooleanField()

    number_of_layers = models.IntegerField()

    price = models.DecimalField(max_digits=5, decimal_places=2)

    flavours = models.ManyToManyField(CakeFlavour)


class CakeImage(models.Model):
    cake = models.ForeignKey(
        IndividualCake, related_name="images", on_delete=models.CASCADE
    )

    image = CloudinaryField("image", folder="just_cakes_images")

    def __str__(self):
        return f"{self.cake.name} Image"


class Cake(models.Model):
    # Define your fields here
    # For example:
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add more fields as needed
