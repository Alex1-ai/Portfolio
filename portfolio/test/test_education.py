
from .test_setup import TestSetup
from ..models import Education
class TestPortfolioViewTestCase(TestSetup):


# MODEL TEST
    def test_education_model_text_content(self):
        education = Education.objects.get(id=1)
        expected_object_degree = f"{education.degree}"
        expected_object_year = f"{education.year}"
        expected_object_university = f"{education.university}"
        expected_object_fieldstudy = f"{education.field_study}"
        expected_object_description = f"{education.description}"
       
        # degree = "Bachelor Degree",
        # year = "2023",
        # university = 'Methodist University',
        # field_study = "Information Technology",
        # description = 'This is a simple description of the Education'
        self.assertEquals(expected_object_degree, "Bachelor Degree")
        self.assertEquals(expected_object_year, "2023")
        self.assertEquals(expected_object_university, 'Methodist University')
        self.assertEquals(expected_object_fieldstudy, "Information Technology")
        self.assertEquals(expected_object_description, 'This is a simple description of the Education')
        

    def test_education_about(self):
        response = self.client.get(self.about_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bachelor Degree")
        self.assertTemplateUsed(response, 'about.html')
    

  