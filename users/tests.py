from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class AuthenticationTests(TestCase):

    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'test_user',
            'password1': 'password123',
            'password2': 'password123',
        })
        self.assertEqual(response.status_code, 302)  # Redirects to 'hello_world' page

    def test_user_login(self):
        user = User.objects.create_user(username='test_user', password='password123')
        response = self.client.post(reverse('login'), {
            'username': 'test_user',
            'password': 'password123',
        })
        self.assertEqual(response.status_code, 302)  # Logs in and redirects to 'hello_world' page

    def test_user_logout(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Logs out and redirects to 'login' page

    def test_access_hello_world_unauthenticated(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 302)  # Unauthorized access fails and redirects to 'login' page

    def test_access_hello_world_authenticated(self):
        user = User.objects.create_user(username='test_user', password='password123')
        self.client.login(username='test_user', password='password123')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)  # Access granted

    def test_incorrect_password(self):
        user = User.objects.create_user(username='testuser', password='password123')
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrong_password',
        })
        self.assertEqual(response.status_code, 200)  # Should return to the login page
        self.assertContains(response, 'Please enter a correct username and password.')

    def test_non_existent_user(self):
        response = self.client.post(reverse('login'), {
            'username': 'nonexistent_user',
            'password': 'password123',
        })
        self.assertEqual(response.status_code, 200)  # Should return to the login page
        self.assertContains(response, 'Please enter a correct username and password.')

    def test_session_fixation(self):
        # Create a session and get the session key
        self.client.get(reverse('login'))
        session_key = self.client.session.session_key

        # Log in with a different user
        user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')

        # Check if the session key has changed
        new_session_key = self.client.session.session_key
        self.assertNotEqual(session_key, new_session_key)

    def test_csrf_attack(self):
        self.client = Client(enforce_csrf_checks=True)  # Enable CSRF checks
        user = User.objects.create_user(username='testuser', password='password123')

        # Craft a malicious POST request with a forged CSRF token
        malicious_data = {
            'username': 'testuser',
            'password': 'password123',
            'csrfmiddlewaretoken': 'malicious_csrf_token',  # Replace with your own forged CSRF token
        }

        response = self.client.post(reverse('login'), malicious_data)
        self.assertEqual(response.status_code, 403)  # Should return a Forbidden response
