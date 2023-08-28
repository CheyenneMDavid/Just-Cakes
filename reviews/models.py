from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# Much in this models.py is from the walkthrough project with Hello Django

STATUS = ((0, "Draft"), (1, "Published"))


class Reviews(models.Model):
    # Ensure that the maximum character length of a title is kept to 100
    # and setting unique to "True", ensures that
    title = models.CharField(max_length=100)
    # Having purposely not enforced title to be unique, still setting unique
    # to True in slug so that any URLs created aren't repeated.
    slug = models.SlugField(max_length=120, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="reviews", null=True
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name="reviews_like", blank=True
    )
    featured_image = CloudinaryField("image", default="placeholder")
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name="reviewspost_like", blank=True
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        """Returns the review title as a string."""
        return self.title

    def number_of_likes(self):
        """Returns the number of likes the reviews got."""

    # Previously, for the title, "unique" was purposely ommitted. But the slug
    # which is used to create a url, still needs to be unique.  So this is
    # going to ensure that when the url is created, it's still in a user
    # friendly manner, despite it coming from a title that is the same as
    # another review.  Because it's more than concieveable that more than one
    # person may want to title a review of their wedding cake
    #  as "Beautiful day".  And to deny them the title choice taints the user
    # experience.
    def save(self, *args, **kwargs):
        """
        Overiding the default way creating a slug from the title which may well
        be the same as another post.
        """
        if not self.slug:  # Creates a slug if it doesn't exist.
            # hands over the job of creating a slug to slugify, which will
            # still uses the title, even if it's the same.  But creates a
            # variation that's still readable by the user.
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
