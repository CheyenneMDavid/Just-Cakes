from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):
    """
    Tests for validating the CommentForm. They ensure that forms with proper
    input are considered valid and forms with missing or incorrect input are
    considered invalid.
    """

    # Testing to check if a comment form is valid
    def test_form_is_valid(self):
        # Comment form with valid input.
        comment_form = CommentForm({"body": "This is a great Post"})
        # Assert that the form is considered valid
        self.assertTrue(
            comment_form.is_valid(),
            msg="The form should be valid with content in the body.",
        )

    # Testing to check if a comment form is invalid
    def test_form_is_invalid(self):
        # Comment form with invalid input (empty body)
        comment_form = CommentForm({"body": ""})
        # Assert that the form is considered invalid
        self.assertFalse(
            comment_form.is_valid(),
            msg="The form should be invalid if the it has an empty body.",
        )
