from django.test import TestCase
from courses.models import Course
from django.utils import timezone
from datetime import date, timedelta
from django.test import Client


class CourseTests(TestCase):

    def test_course_create(self):
        course1 = Course.objects.create(name='PyBursa02',
                                        start_date=date(2015, 2, 16))
        course2 = Course.objects.create(name='JsBursa03',
                                        start_date=date(2015, 2, 2))

        self.assertEqual(Course.objects.all().count(), 2)

    def test_is_in_future(self):
        date_in_future = timezone.now().date() + timedelta(days=1)
        date_in_past = timezone.now().date() - timedelta(days=1)
        course_today = Course.objects.create(name='PyBursa01',
                                             start_date=timezone.now().date())
        self.assertEqual(course_today.is_in_future(), False)

        course_future = Course.objects.create(name='PyBursa02',
                                              start_date=date_in_future)
        self.assertTrue(course_future.is_in_future())

        course_past = Course.objects.create(name='PyBursa03',
                                            start_date=date_in_past)
        self.assertFalse(course_past.is_in_future())

    def test_pages(self):
        client = Client()

        response = client.get('/courses/')
        self.assertEqual(response.status_code, 200)

        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
        course1 = Course.objects.create(name='PyBursa02',
                                        start_date=date(2015, 2, 16))

        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "PyBursa02")

from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

class MySeleniumTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(MySeleniumTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()

    def test_courses(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/courses/'))
        import time
        time.sleep(10)

        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        time.sleep(10)
        
        self.selenium.get('%s%s' % (self.live_server_url, '/students/'))
        time.sleep(10)
        
        # username_input = self.selenium.find_element_by_name("username")
        # username_input.send_keys('myuser')
        # password_input = self.selenium.find_element_by_name("password")
        # password_input.send_keys('secret')
        # self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
