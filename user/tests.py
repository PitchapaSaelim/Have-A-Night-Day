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
        response = self.client.post(reverse("register_user"),{'username':'Parn', 'fname':'Panida', 'lname':'Ounnaitham', 'birth_date':'2000-11-02', 'gender':'Female', 'password1':'Saiparn021143', 'password2':'Saiparn021143'})
        self.assertEqual(response.status_code, 302)

    def test_authenticate_user(self):
        self.client.login(username='Saiparn',password='@Parn123') 
        self.assertIn('_auth_user_id', self.client.session)
    
    def test_unauthenticate_user(self):
        """Test if the user does not login."""
        with self.assertRaises(AssertionError):
            self.assertIn('_auth_user_id', self.client.session)

    def test_access_to_home_page_with_authenticated_user(self):
        """Test if authenticated user can access home page."""
        self.client.login(username='Saiparn',password='@Parn123')  
        response = self.client.get(reverse("sleep_time_management:home"))
        self.assertEqual(response.status_code, 200)

    def test_access_to_main_profile_with_authenticated_user(self):
        """Test if authenticated user can access main profile page."""
        self.client.login(username='Saiparn',password='@Parn123')  
        response = self.client.get(reverse("sleep_time_management:mainprofile"))
        self.assertEqual(response.status_code, 200)

    def test_access_to_edit_profile_with_authenticated_user(self):
        """Test if authenticated user can access main editprofile page."""
        self.client.login(username='Saiparn',password='@Parn123')  
        response = self.client.get(reverse("sleep_time_management:editprofile"))
        self.assertEqual(response.status_code, 200)

    def test_access_to_information_with_authenticated_user(self):
        """Test if authenticated user can access information page."""
        self.client.login(username='Saiparn',password='@Parn123')  
        response = self.client.get(reverse("sleep_time_management:information"))
        self.assertEqual(response.status_code, 200)
    
    def test_access_to_home_page_with_unauthenticated_user(self):
        """Test if unauthenticated user cannot access home page.""" 
        response = self.client.get(reverse("sleep_time_management:home"))
        self.assertEqual(response.status_code, 302)

    def test_access_to_main_profile_with_unauthenticated_user(self):
        """Test if unauthenticated user cannot access main profile page.""" 
        response = self.client.get(reverse("sleep_time_management:mainprofile"))
        self.assertEqual(response.status_code, 302)

    def test_access_to_edit_profile_with_unauthenticated_user(self):
        """Test if unauthenticated user cannot access main editprofile page."""  
        response = self.client.get(reverse("sleep_time_management:editprofile"))
        self.assertEqual(response.status_code, 302)

    def test_access_to_information_with_unauthenticated_user(self):
        """Test if unauthenticated user cannot access information page.""" 
        response = self.client.get(reverse("sleep_time_management:information"))
        self.assertEqual(response.status_code, 302)

    def test_access_to_home_page_if_user_logout(self):
        """Test if user cannot access home page if user logout.""" 
        self.client.login(username='Saiparn',password='@Parn123')
        self.client.logout()
        response = self.client.get(reverse("sleep_time_management:home"))
        self.assertEqual(response.status_code, 302)

    def test_access_to_main_profile_if_user_logout(self):
        """Test if user cannot access main profile page if user logout.""" 
        self.client.login(username='Saiparn',password='@Parn123')
        self.client.logout()
        response = self.client.get(reverse("sleep_time_management:mainprofile"))
        self.assertEqual(response.status_code, 302)

    def test_access_to_edit_profile_if_user_logout(self):
        """Test if user cannot access edit profile page if user logout."""
        self.client.login(username='Saiparn',password='@Parn123')
        self.client.logout()
        response = self.client.get(reverse("sleep_time_management:editprofile"))
        self.assertEqual(response.status_code, 302)

    def test_access_to_information_if_user_logout(self):
        """Test if user cannot access information page if user logout."""
        self.client.login(username='Saiparn',password='@Parn123')
        self.client.logout()
        response = self.client.get(reverse("sleep_time_management:information"))
        self.assertEqual(response.status_code, 302)

    def test_cannot_access_to_home_page_if_login_with_out_username(self):
        """Test user cannot access home page if user login with out username"""
        self.client.login(username='',password='@Parn123')
        response = self.client.get(reverse("sleep_time_management:home"))
        self.assertEqual(response.status_code, 302)

    def test_cannot_access_to_home_page_if_login_with_out_password(self):
        """Test user cannot access home page if user login with out password"""
        self.client.login(username='Saiparn',password='')
        response = self.client.get(reverse("sleep_time_management:home"))
        self.assertEqual(response.status_code, 302)


    