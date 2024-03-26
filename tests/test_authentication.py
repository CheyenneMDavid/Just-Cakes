from django.test import TestCase
from django.urls import reverse


class AuthenticationTests(TestCase):
    """
    Testing for signup, login, and
    logout which is handled by allauth
    """

    def test_new_user_signup(self):
        """
        Testing new user signing-up.
        """
        signup_url = reverse("account_signup")
        response = self.client.get(signup_url)
        self.assertEqual(response.status_code, 200)

    def test_user_sign_in(self):
        """
        Testing user signing-in.
        """
        login_url = reverse("account_login")
        response = self.client.get(login_url)
        self.assertEqual(response.status_code, 200)

    def test_user_sign_out(self):
        """
        Testing user signing-out.
        """
        logout_url = reverse("account_login")
        response = self.client.get(logout_url)
        self.assertEqual(response.status_code, 200)
