"""
Much of this model has been copied or has been influenced by the django
Codestar Blog walkthrough project with Code Institute.

Using slugify so that if a user writes a post with a same title, it's doesn't 
clash.  Slugify generates an alternative that can be read easily
"""

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


# Defines the status for the post
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Model representing a post.
    """

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post", null=True
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = CloudinaryField("image", default="placeholder")
    updated_on = models.DateTimeField(
        auto_now=True,
    )
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        """
        String representation of the Post object.
        """
        return str(self.title)

    def number_of_likes(self):
        """
        Counts the number of likes for a post.
        """
        return self.likes.count()

    def save(self, *args, **kwargs):
        """
        Override the save method to generate a unique slug.
        """
        # Generate a slug from the post title
        if not self.slug:
            self.slug = slugify(self.title)

        # Ensure the slug is unique
        original_slug = self.slug
        counter = 1
        while Post.objects.filter(slug=self.slug).exists():
            self.slug = f"{original_slug}-{counter}"
            counter += 1

        super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Model representing a comment on a post.
    """

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    # Author field added to enable update and delete of comments.
    # But using "comment_author" as the variable to ensure against mix-up
    comment_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments", null=True
    )

    class Meta:
        """
        Meta class for configuring order of comments according to creation
        date, in descending order.
        """

        ordering = ["created_on"]

    def __str__(self):
        """
        String representation of the Post object.
        """
        return f"Comment {self.body} by {self.name}"
