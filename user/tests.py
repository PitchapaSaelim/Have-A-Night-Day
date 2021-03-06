"""Test for User."""
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class AuthorModelTest(TestCase):
    """Class to test feature about AuthorModel."""

    def setUp(self):
        """Set up for testcase."""
        User = get_user_model()
        user = User.objects.create_user(
            username='Saiparn', password='@Parn123')
        user.first_name = 'Panida'
        user.last_name = 'Ounnaitham'
        user.save()

    def test_user_name_in_database(self):
        """Test if user name is in database."""
        user = User.objects.filter(username='Saiparn').first()
        self.assertEqual(user.username, 'Saiparn')

    def test_addAccount(self):
        """Test if register page is work."""
        response = self.client.post(reverse("register_user"), {'username': 'Parn', 'fname': 'Panida', 'lname': 'Ounnaitham',
                                                               'birth_date': '2000-11-02', 'gender': 'Female', 'password1': 'Saiparn021143', 'password2': 'Saiparn021143'})
        self.assertEqual(response.status_code, 302)

    def test_authenticate_user(self):
        """Test if authenticated user is log in."""
        self.client.login(username='Saiparn', password='@Parn123')
        self.assertIn('_auth_user_id', self.client.session)

    def test_unauthenticate_user(self):
        """Test if the user does not login."""
        with self.assertRaises(AssertionError):
            self.assertIn('_auth_user_id', self.client.session)

    def test_access_to_home_page_with_authenticated_user(self):
        """Test if authenticated user can access home page."""
        self.client.login(username='Saiparn', password='@Parn123')
        response = self.client.get(reverse("sleep_time_management:home"))
        self.assertEqual(response.status_code, 200)

    def test_access_to_about_us_with_authenticated_user(self):
        """Test if authenticated user can access about us page."""
        self.client.login(username='Saiparn', password='@Parn123')
        response = self.client.get(reverse("sleep_time_management:about_us"))
        self.assertEqual(response.status_code, 200)

    def test_access_to_contact_us_with_authenticated_user(self):
        """Test if authenticated user can access contact us page."""
        self.client.login(username='Saiparn', password='@Parn123')
        response = self.client.get(reverse("sleep_time_management:contact_us"))
        self.assertEqual(response.status_code, 200)

    def test_access_to_edit_profile_with_authenticated_user(self):
        """Test if authenticated user can access main editprofile page."""
        self.client.login(username='Saiparn', password='@Parn123')
        response = self.client.get(
            reverse("sleep_time_management:editprofile"))
        self.assertEqual(response.status_code, 200)

    def test_access_to_information_with_authenticated_user(self):
        """Test if authenticated user can access information page."""
        self.client.login(username='Saiparn', password='@Parn123')
        response = self.client.get(
            reverse("sleep_time_management:information"))
        self.assertEqual(response.status_code, 200)

    def test_access_to_home_page_with_unauthenticated_user(self):
        """Test if unauthenticated user cannot access home page."""
        response = self.client.get(reverse("sleep_time_management:home"))
        self.assertEqual(response.status_code, 302)

    def test_access_to_main_profile_with_unauthenticated_user(self):
        """Test if unauthenticated user cannot access main profile page."""
        response = self.client.get(
            reverse("sleep_time_management:mainprofile"))
        self.assertEqual(response.status_code, 302)

    def test_access_to_about_us_with_unauthenticated_user(self):
        """Test if unauthenticated user cannot access home page."""
        response = self.client.get(reverse("sleep_time_management:about_us"))
        self.assertEqual(response.status_code, 200)

    def test_access_to_contact_us_with_unauthenticated_user(self):
        """Test if unauthenticated user cannot access main profile page."""
        response = self.client.get(reverse("sleep_time_management:contact_us"))
        self.assertEqual(response.status_code, 200)

    def test_access_to_edit_profile_with_unauthenticated_user(self):
        """Test if unauthenticated user cannot access main editprofile page."""
        response = self.client.get(
            reverse("sleep_time_management:editprofile"))
        self.assertEqual(response.status_code, 302)

    def test_access_to_information_with_unauthenticated_user(self):
        """Test if unauthenticated user cannot access information page."""
        response = self.client.get(
            reverse("sleep_time_management:information"))
        self.assertEqual(response.status_code, 200)

    def test_access_to_home_page_if_user_logout(self):
        """Test if user cannot access home page if user logout."""
        self.client.login(username='Saiparn', password='@Parn123')
        self.client.logout()
        response = self.client.get(reverse("sleep_time_management:home"))
        self.assertEqual(response.status_code, 302)

    def test_access_to_main_profile_if_user_logout(self):
        """Test if user cannot access main profile page if user logout."""
        self.client.login(username='Saiparn', password='@Parn123')
        self.client.logout()
        response = self.client.get(
            reverse("sleep_time_management:mainprofile"))
        self.assertEqual(response.status_code, 302)

    def test_access_to_edit_profile_if_user_logout(self):
        """Test if user cannot access edit profile page if user logout."""
        self.client.login(username='Saiparn', password='@Parn123')
        self.client.logout()
        response = self.client.get(
            reverse("sleep_time_management:editprofile"))
        self.assertEqual(response.status_code, 302)

    def test_access_to_information_if_user_logout(self):
        """Test if user cannot access information page if user logout."""
        self.client.login(username='Saiparn', password='@Parn123')
        self.client.logout()
        response = self.client.get(
            reverse("sleep_time_management:information"))
        self.assertEqual(response.status_code, 200)

    def test_access_to_contact_us_if_user_logout(self):
        """Test if user cannot access contact us page if user logout."""
        self.client.login(username='Saiparn', password='@Parn123')
        self.client.logout()
        response = self.client.get(reverse("sleep_time_management:contact_us"))
        self.assertEqual(response.status_code, 200)

    def test_access_to_about_us_if_user_logout(self):
        """Test if user cannot access about us page if user logout."""
        self.client.login(username='Saiparn', password='@Parn123')
        self.client.logout()
        response = self.client.get(reverse("sleep_time_management:about_us"))
        self.assertEqual(response.status_code, 200)

    def test_cannot_access_to_home_page_if_login_with_out_username(self):
        """Test user cannot access home page if user login with out username."""
        self.client.login(username='', password='@Parn123')
        response = self.client.get(reverse("sleep_time_management:home"))
        self.assertEqual(response.status_code, 302)

    def test_cannot_access_to_home_page_if_login_with_out_password(self):
        """Test user cannot access home page if user login with out password."""
        self.client.login(username='Saiparn', password='')
        response = self.client.get(reverse("sleep_time_management:home"))
        self.assertEqual(response.status_code, 302)

    def test_regis_with_wrong_gender(self):
        """Test user cannot regis if user input wrong gender format."""
        response = self.client.post(reverse("register_user"), {'username': 'Parn', 'fname': 'Panida', 'lname': 'Ounnaitham',
                                                               'birth_date': '2000-11-02', 'gender': 'fhwiv', 'password1': 'Saiparn021143', 'password2': 'Saiparn021143'})
        # cannot register because wrong gender so not redirect
        self.assertEqual(response.status_code, 200)

    def test_regis_with_wrong_birthday(self):
        """Test user cannot regis if user input wrong birthday format,birthday is in the future."""
        response = self.client.post(reverse("register_user"), {'username': 'Parn', 'fname': 'Panida', 'lname': 'Ounnaitham',
                                                               'birth_date': '2034-11-02', 'gender': 'fhwiv', 'password1': 'Saiparn021143', 'password2': 'Saiparn021143'})
        # cannot register because wrong birth date so not redirect
        self.assertEqual(response.status_code, 200)
