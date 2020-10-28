from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from .models import Author


class AuthorModelTest(TestCase):
    
    def test_user_name_in_database(self):
        User.objects.create_user(username='Big',password='@Parn123')
        user1 = User.objects.filter(username='Big').first()
        self.assertEqual(user1.username,'Big')

    def test_first_name_max_length(self):
        User.objects.create(first_name='Big', last_name='Bob')
        author = User.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 150)

    def test_addAccount(self):
        response = self.client.post(reverse("register_user"),{'username':'Parn', 'fname':'Panida', 'lname':'Ounnaitham', 'password1':'Saiparn021143', 'password2':'Saiparn021143'})
        self.assertEqual(response.status_code, 302)

    