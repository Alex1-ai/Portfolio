
from .test_setup import TestSetup
from ..models import Personal_Information


class TestPersonalInfoViewTestCase(TestSetup):


        #   first_name = "test_first_name",
        #     last_name = "test_last_name",
        #     profession = "test_software_engineer",
        #     nationality = "test_nationality",
        #     freelance = "test_freelancing",
        #     address = "test_addresses",
        #     phone = "0503289832",
        #     email = "test@gmail.com",
        #     github = "https://www.github/test",
        #     langauges = "English",
        #     cv = "media\documents\Onedibe_Emmanuel_Fullstack_Engineer2.pdf"
# MODEL TEST
    def test_personal_info_model_text_content(self):
        personal_info = Personal_Information.objects.get(id=1)
        expected_object_first_name = personal_info.first_name
        expected_object_last_name = personal_info.last_name
        expected_object_profession = personal_info.profession
        expected_object_nationality = personal_info.nationality
        expected_object_freelance = personal_info.freelance
        expected_object_address = personal_info.address
        expected_object_email = personal_info.email
        expected_object_phone = personal_info.phone
        expected_object_github = personal_info.github
        expected_object_languages = personal_info.langauges

       
       
        self.assertEquals(expected_object_first_name, "test_first_name")
        self.assertEquals(expected_object_last_name, "test_last_name")
        self.assertEquals(expected_object_profession, "test_software_engineer")
        self.assertEquals(expected_object_nationality, "test_nationality")
        self.assertEquals(expected_object_email,"test@gmail.com" )
        self.assertEquals(expected_object_github, "https://www.github/test")
        self.assertEquals(expected_object_phone, "0503289832")
        self.assertEquals(expected_object_languages,"English" )
        self.assertEquals(expected_object_freelance, "test_freelancing")
        self.assertEquals(expected_object_address, "test_addresses")
        
    #   first_name = "test_first_name",
        #     last_name = "test_last_name",
        #     profession = "test_software_engineer",
        #     nationality = "test_nationality",
        #     freelance = "test_freelancing",
        #     address = "test_addresses",
        #     phone = "0503289832",
        #     email = "test@gmail.com",
        #     github = "https://www.github/test",
        #     langauges = "English",
    def test_personal_info_displayed_in_about_page(self):
        response = self.client.get(self.about_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test_first_name")
        self.assertContains(response, "test_last_name")
        self.assertContains(response, "test_nationality")
        self.assertContains(response, "test_freelancing")
        self.assertContains(response, "test_addresses")
        self.assertContains(response, "0503289832")
        self.assertContains(response, "test@gmail.com")
        self.assertContains(response, "https://www.github/test")
        self.assertContains(response, "English")
        self.assertTemplateNotUsed(response, 'blog-detail.html')
    

  