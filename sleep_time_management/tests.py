"""Test for sleep time management."""
from sleep_time_management.models import calculate_sleep_bed, calculate_sleep_wake
from sleep_time_management.views import calculate_sleeptime, calculate_waketime, get_age_span, get_disease_list, get_sleep_hour
from django.test import TestCase


class CalculateViewsTest(TestCase):
    """Class to test feature about CalculateViews."""

    def test_calculate_wakeup_time(self): 
        """Test when user input wake up time and application can calculate sleep time correctly."""
        sleeptime = ['22:30', '21:00', '19:30', '18:00', '16:30', '15:00']
        sleep_time_from_app = calculate_waketime('00:00')
        self.assertListEqual(sleeptime, sleep_time_from_app)

    def test_sleep_time(self):
        """Test when user input sleep time and application can calculate wake up time correctly."""
        wake_up_time = ['23:30', '1:00', '2:30', '4:00', '5:30', '7:00']
        wake_up_time_from_app = calculate_sleeptime('22:00')
        self.assertListEqual(wake_up_time, wake_up_time_from_app)

    def test_sleep_time_data_wake_time(self):
        """Test when user input wake up time and select bed time,application can calculate sleep data correctly."""
        sleep_data = '7.30 hours'
        sleep_data_from_app = calculate_sleep_wake(360, 1350)
        self.assertEqual(sleep_data, sleep_data_from_app)

    def test_sleep_time_data_bed_time(self):
        """Test when user input bed time and select wake up time,application can calculate sleep data correctly."""
        sleep_data = '1.30 hours'
        sleep_data_from_app = calculate_sleep_bed(120, 210)
        self.assertEqual(sleep_data, sleep_data_from_app)

    def test_age_span_toddler(self):
        """Test when user input age, and application can give toddler age span correctly."""
        toddler = 'Toddler'
        toddler_from_app = get_age_span(1)
        self.assertEqual(toddler, toddler_from_app)

    def test_age_span_preschool(self):
        """Test when user input age, and application can give preschool age span correctly."""
        preschool = 'Preschool'
        preschool_from_app = get_age_span(4)
        self.assertEqual(preschool, preschool_from_app)

    def test_age_span_school_age(self):
        """Test when user input age, and application can give school age age span correctly."""
        school_age = 'School age'
        school_age_from_app = get_age_span(12)
        self.assertEqual(school_age, school_age_from_app)

    def test_age_span_teenager(self):
        """Test when user input age, and application can give teenager age span correctly."""
        teenager = 'Teenager'
        teenager_from_app = get_age_span(16)
        self.assertEqual(teenager, teenager_from_app)

    def test_age_span_young_adult(self):
        """Test when user input age, and application can give young adult age span correctly."""
        young_adult = 'Young adult'
        young_adult_from_app = get_age_span(20)
        self.assertEqual(young_adult, young_adult_from_app)

    def test_age_span_adult(self):
        """Test when user input age, and application can give adult age span correctly."""
        adult = 'Adult'
        adult_from_app = get_age_span(50)
        self.assertEqual(adult, adult_from_app)

    def test_age_span_young_older_adult(self):
        """Test when user input age, and application can give older adult age span correctly."""
        older_adult = 'Older adult'
        older_adult_from_app = get_age_span(70)
        self.assertEqual(older_adult, older_adult_from_app)

    def test_get_sleep_hour_toddler(self):
        """Test when user input toddler age span, and application can suggest sleep hour correctly."""
        sleep_hour = '11-14 hours'
        sleep_hour_from_app = get_sleep_hour('Toddler')
        self.assertEqual(sleep_hour, sleep_hour_from_app)

    def test_get_sleep_hour_preschool(self):
        """Test when user input preschool age span, and application can suggest sleep hour correctly."""
        sleep_hour = '10-13 hours'
        sleep_hour_from_app = get_sleep_hour('Preschool')
        self.assertEqual(sleep_hour, sleep_hour_from_app)

    def test_get_sleep_hour_school_age(self):
        """Test when user input school age span, and application can suggest sleep hour correctly."""
        sleep_hour = '9-11 hours'
        sleep_hour_from_app = get_sleep_hour('School age')
        self.assertEqual(sleep_hour, sleep_hour_from_app)

    def test_get_sleep_hour_teenager(self):
        """Test when user input teenager age span, and application can suggest sleep hour correctly."""
        sleep_hour = '8-10 hours'
        sleep_hour_from_app = get_sleep_hour('Teenager')
        self.assertEqual(sleep_hour, sleep_hour_from_app)

    def test_get_sleep_hour_young_adult(self):
        """Test when user input young adult age span, and application can suggest sleep hour correctly."""
        sleep_hour = '7-9 hours'
        sleep_hour_from_app = get_sleep_hour('Young adult')
        self.assertEqual(sleep_hour, sleep_hour_from_app)

    def test_get_sleep_hour_adult(self):
        """Test when user input adult age span, and application can suggest sleep hour correctly."""
        sleep_hour = '7-9 hours'
        sleep_hour_from_app = get_sleep_hour('Adult')
        self.assertEqual(sleep_hour, sleep_hour_from_app)

    def test_get_sleep_hour_older_adult(self):
        """Test when user input older adult age span, and application can suggest sleep hour correctly."""
        sleep_hour = '7-8 hours'
        sleep_hour_from_app = get_sleep_hour('Older adult')
        self.assertEqual(sleep_hour, sleep_hour_from_app)

    def test_get_disease_list_Hypertension(self):
        """Test when user input age, gender, sleep hour, and application can suggest disease correctly."""
        Hypertension = 'Hypertension'
        get_disease = get_disease_list(30, "Female", 3)
        self.assertTrue(Hypertension in get_disease)

    def test_get_disease_list_Hypertension_old(self):
        """Test when user input age, gender, sleep hour, and application can suggest disease correctly."""
        Hypertension = 'Hypertension'
        get_disease = get_disease_list(65, "Female", 10)
        self.assertTrue(Hypertension in get_disease)

    def test_get_disease_list_Breast_cancer(self):
        """Test when user input age, gender, sleep hour, and application can suggest disease correctly."""
        Disease = "Breast cancer risk"
        get_disease = get_disease_list(65, "Female", 11)
        self.assertTrue(Disease in get_disease)

    def test_get_disease_list_CHD_Female(self):
        """Test when user input age, gender, sleep hour, and application can suggest disease correctly."""
        Disease = "Coronary heart disease (CHD)"
        get_disease = get_disease_list(15, "Female", 5)
        self.assertTrue(Disease in get_disease)

    def test_get_disease_list_Depression(self):
        """Test when user input age, gender, sleep hour, and application can suggest disease correctly."""
        Disease = "Depression"
        get_disease = get_disease_list(67, "Female", 4)
        self.assertTrue(Disease in get_disease)

    def test_get_disease_list_Infertility(self):
        """Test when user input age, gender, sleep hour, and application can suggest disease correctly."""
        Disease = "Infertility"
        get_disease = get_disease_list(67, "Female", 10)
        self.assertTrue(Disease in get_disease)

    def test_get_disease_list_CHD_Male(self):
        """Test when user input age, gender, sleep hour, and application can suggest disease correctly."""
        Disease = "Coronary heart disease (CHD)"
        get_disease = get_disease_list(45, "Male", 4)
        self.assertTrue(Disease in get_disease)

    def test_get_disease_list_REM(self):
        """Test when user input age, gender, sleep hour, and application can suggest disease correctly."""
        Disease = "REM Sleep Disorder"
        get_disease = get_disease_list(55, "Male", 4)
        self.assertTrue(Disease in get_disease)

    def test_get_disease_list_IGT(self):
        """Test when user input age, gender, sleep hour, and application can suggest disease correctly."""
        Disease = "Diabetes mellitus (DM) /Impaired glucose tolerance (IGT)"
        get_disease = get_disease_list(55, "Male", 4)
        self.assertTrue(Disease in get_disease)

    def test_get_disease_list_Stroke(self):
        """Test when user input age, gender, sleep hour, and application can suggest disease correctly."""
        Disease = "Stroke"
        get_disease = get_disease_list(20, "Male", 4)
        self.assertTrue(Disease in get_disease)

    def test_get_disease_list_Colorectal(self):
        """Test when user input age, gender, sleep hour, and application can suggest disease correctly."""
        Disease = "Colorectal cancer"
        get_disease = get_disease_list(20, "Male", 4)
        self.assertTrue(Disease in get_disease)

    def test_get_disease_list_Hypersomnia(self):
        """Test when user input age, gender, sleep hour, and application can suggest disease correctly."""
        Disease = "Hypersomnia"
        get_disease = get_disease_list(20, "Male", 9)
        self.assertTrue(Disease in get_disease)

    def test_get_disease_list_Male(self):
        """Test when user is a male input age, sleep hour, and application can suggest disease correctly."""
        get_disease = get_disease_list(20, "Male", 9)
        Disease = [
            'Diabetes mellitus (DM) /Impaired glucose tolerance (IGT)', 'Hypersomnia']
        self.assertEqual(get_disease, Disease)

    def test_get_disease_list_Female(self):
        """Test when user is a female input age, sleep hour, and application can suggest disease correctly."""
        get_disease = get_disease_list(67, "Female", 4)
        Disease = ['Depression', 'Colorectal cancer']
        self.assertEqual(get_disease, Disease)
