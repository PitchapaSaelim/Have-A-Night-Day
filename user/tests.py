from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib import auth



class AuthorModelTest(TestCase):


    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(username='Saiparn',password='@Parn123')
        user.first_name = 'Panida'
        user.last_name = 'Ounnaitham'
        user.save()
    
    def test_user_name_in_database(self):
        # User.objects.create_user(username='Big',password='@Parn123')
        user = User.objects.filter(username='Saiparn').first()
        self.assertEqual(user.username,'Saiparn')

    def test_addAccount(self):
        response = self.client.post(reverse("register_user"),{'username':'Parn', 'fname':'Panida', 'lname':'Ounnaitham', 'password1':'Saiparn021143', 'password2':'Saiparn021143'})
        self.assertEqual(response.status_code, 302)

    def test_authenticate_user(self):
        self.client.login(username='Saiparn',password='@Parn123') 
        self.assertIn('_auth_user_id', self.client.session)
    
    def test_unauthenticate_user(self):
        """Test if the user does not login."""
        with self.assertRaises(AssertionError):
            self.assertIn('_auth_user_id', self.client.session)