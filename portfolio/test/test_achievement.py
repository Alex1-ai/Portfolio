
from .test_setup import TestSetup
from ..models import Achievement


class TestPortfolioViewTestCase(TestSetup):


        # years_of_experience = 5,
        # completed_projects = 45,
        # happy_customers = 50,
        # awards = 30

# MODEL TEST
    def test_achievement_model_text_content(self):
        achievement = Achievement.objects.get(id=1)
        expected_object_year_of_experience = achievement.years_of_experience
        expected_object_completed_projects = achievement.completed_projects
        expected_object_happy_customer = achievement.happy_customers
        expected_object_awards = achievement.awards

       
       
        self.assertEquals(expected_object_year_of_experience, 5)
        self.assertEquals(expected_object_completed_projects, 45)
        self.assertEquals(expected_object_happy_customer, 50)
        self.assertEquals(expected_object_awards, 30)
        

    def test_achievement_displayed_in_about(self):
        response = self.client.get(self.about_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 5)
        self.assertContains(response, 45)
        self.assertContains(response, 50)
        self.assertContains(response, 30)
        self.assertTemplateUsed(response, 'about.html')
    

  