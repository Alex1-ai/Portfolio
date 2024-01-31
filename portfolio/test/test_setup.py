# from rest_framework.test import APITestCase
from django.test import TestCase
from django.urls import reverse
from faker import Faker
from ..models import Portfolio, Skills, Contact, Education, Experience, Achievement, Personal_Information
class TestSetup(TestCase):
    def setUp(self):
        self.home_url = reverse('home')
        self.about_url = reverse('about')
        self.portfolio_url = reverse('portfolio')
        self.contact_url = reverse('contact')
        # self.login_url = reverse('login')
        self.fake = Faker()
        

        
        # self.user_data={
        #     "email":self.fake.email(),
        #     "username":self.fake.email().split("@")[0],
        #     "password":self.fake.email()
        # }

        Portfolio.objects.create(
            title = "Test Portfolio",
            langauge = "English",
            link = "https://www.oce-markt.com",
            client = "Freelance",
            project_type = "Web Application",
            image = "media/blog/softwareEngi.jpg"
        )

        Education.objects.create(
            degree = "Bachelor Degree",
            year = "2023",
            university = 'Methodist University',
            field_study = "Information Technology",
            description = 'This is a simple description of the Education'
        )

        Experience.objects.create(
            year = '2021',
            company = "oce-markt",
            position = "Fullstack Developer",
            description = "This is the description of the Experience"

        ),
        Personal_Information.objects.create(
            first_name = "test_first_name",
            last_name = "test_last_name",
            profession = "test_software_engineer",
            nationality = "test_nationality",
            freelance = "test_freelancing",
            address = "test_addresses",
            phone = "0503289832",
            email = "test@gmail.com",
            github = "https://www.github/test",
            langauges = "English",
            cv = "media\documents\Onedibe_Emmanuel_Fullstack_Engineer2.pdf"

        )
        Achievement.objects.create(
             years_of_experience = 5,
            completed_projects = 45,
            happy_customers = 50,
            awards = 30
        )
        Contact.objects.create(
            name = "jude",
            subject = "Hiring",
            email = "test@gmail.com",
            message = "This is the test of the contact"
        )

        Skills.objects.create(
            name="python",
            level=30
        )
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()