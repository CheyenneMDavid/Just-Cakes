# Imports the required modules and models.
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# Importing and using "get_user_model" to allow flexibility and easier
# maintenance of the code in the future.
User = get_user_model()

STATUS = ((0, "Draft"), (1, "Published"))


# Much in this file is from the walkthrough project with Hello Django
# Had to change names defining singular and plural to make more sense, both
# here and in other places throughout files.
# Also, have changed "review" to "post" for consistency and to fit with how
# django handles things.


class Post(models.Model):
    """Handles structure and content of posts"""

    # Ensure that the maximum character length of a title is kept to 100.
    title = models.CharField(max_length=100)

    # Having purposely not enforced title to be unique, still setting unique
    # to True in slug so that any URLs created aren't repeated.
    slug = models.SlugField(max_length=120, unique=True)

    # Author of the post is connected to the user model.
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="post",
        null=True,
    )
    # Content of the post.
    content = models.TextField()
    # Sets the date and time the post was created on.
    created_on = models.DateTimeField(auto_now_add=True)

    # Status of whether the post is published or not. Default is set to draft.
    status = models.IntegerField(choices=STATUS, default=0)

    # Featured image for the post, storage used is Cloudinary.
    featured_image = CloudinaryField("image", default="placeholder")

    # small excerpt of the post used in the list of posts.
    excerpt = models.TextField(blank=True)

    # Last date that the post was updated
    updated_on = models.DateTimeField(auto_now=True)

    # Users that have liked the post.
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)

    class Meta:
        """
        Uses the meta data to return posts with the newest ones first by
        using "-" before the created_on.
        """

        ordering = ["-created_on"]

    def __str__(self):
        """Returns the post title as a string."""
        return str(self.title)

    def number_of_likes(self):
        """Returns the number of likes the post has received."""
        # Disabling pylint because the warning is a linter issue and distracting.
        return self.likes.count()  # pylint: disable=no-member

    # Previously, for the title, "unique" was purposely omitted. But the slug
    # which is used to create a url, still needs to be unique.  So this is
    # going to ensure that when the url is created, it's still in a user
    # friendly manner, despite it coming from a title that is the same as
    # another post.  Because it's more than conceivable that more than one
    # person may want to title a post of their wedding cake
    #  as "Beautiful day".  And to deny them the title choice taints the user
    # experience.
    def save(self, *args, **kwargs):
        """
        Overriding the default way creating a slug from the title which may
        well be the same as another post.
        """
        if not self.slug:  # Creates a slug if it doesn't exist.
            # hands over the job of creating a slug to slugify, which will
            # still uses the title, even if it's the same.  But creates a
            # variation that's still readable by the user.
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
