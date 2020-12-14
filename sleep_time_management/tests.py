from sleep_time_management.models import calculate_sleep_bed, calculate_sleep_wake
from sleep_time_management.views import calculate_sleeptime, calculate_waketime
from django.test import TestCase

class CalculateViewsTest(TestCase):
    
    def test_calculate_wakeup_time(self):
        """Test when user input wake up time and application can calculate sleep time correctly """
        sleeptime = ['22:30','21:00','19:30','18:00','16:30','15:00']
        sleep_time_from_app = calculate_waketime('00:00')
        self.assertListEqual(sleeptime, sleep_time_from_app)

    def test_sleep_time(self):
        """Test when user input sleep time and application can calculate wake up time correctly """
        wake_up_time = ['23:30','1:00','2:30','4:00','5:30','7:00']
        wake_up_time_from_app = calculate_sleeptime('22:00')
        self.assertListEqual(wake_up_time,wake_up_time_from_app)

    def test_sleep_time_data_wake_time(self):
        """Test when user input wake up time and select bed time, application can calculate sleep data correctly"""
        sleep_data = '7.30 hours'
        sleep_data_from_app = calculate_sleep_wake(360,1350)
        self.assertEqual(sleep_data,sleep_data_from_app)

    def test_sleep_time_data_bed_time(self):
        """Test when user input bed time and select wake up time, application can calculate sleep data correctly"""
        sleep_data = '1.30 hours'
        sleep_data_from_app = calculate_sleep_bed(120,210)
        self.assertEqual(sleep_data,sleep_data_from_app)


