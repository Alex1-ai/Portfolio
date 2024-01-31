
from .test_setup import TestSetup
from ..models import Experience
class TestPortfolioViewTestCase(TestSetup):


# year = models.CharField(max_length=255)
#     company = models.CharField(max_length=255)
#     position = models.CharField(max_length=255)
#     description = models.TextField()

# MODEL TEST
    def test_experience_model_text_content(self):
        experience = Experience.objects.get(id=1)
        expected_object_year = f"{experience.year}"
        expected_object_company = f"{experience.company}"
        expected_object_position = f"{experience.position}"
        expected_object_description = f"{experience.description}"

       
       
        self.assertEquals(expected_object_year, '2021')
        self.assertEquals(expected_object_company, "oce-markt")
        self.assertEquals(expected_object_position, "Fullstack Developer")
        self.assertEquals(expected_object_description, "This is the description of the Experience")
        

    def test_experience_displayed_in_about(self):
        response = self.client.get(self.about_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "oce-markt")
        self.assertContains(response, "Fullstack Developer")
        self.assertContains(response, "This is the description of the Experience")
        self.assertTemplateUsed(response, 'about.html')
    

  