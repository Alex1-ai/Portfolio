
from .test_setup import TestSetup
from ..models import Skills
class TestPortfolioViewTestCase(TestSetup):


# MODEL TEST
    def test_skills_model_text_content(self):
        skill = Skills.objects.get(id=1)
        expected_object_name = f"{skill.name}"
        expected_object_level = f"{skill.level}"
       

        self.assertEquals(expected_object_name, "python")
        self.assertEquals(int(expected_object_level), 30)
        self.assertNotEquals(expected_object_name, "javascript")
        self.assertNotEquals(expected_object_level, 60)
        
    

  