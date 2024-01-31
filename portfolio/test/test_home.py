
from .test_setup import TestSetup


class TestHomeViewTestCase(TestSetup):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_home_view_url_by_name(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)

    def test_home_view_uses_correct_template(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


    def test_home_page_contains_correct_html(self):
        response = self.client.get(self.home_url)
        self.assertContains(response, """<h1 class="text-uppercase poppins-font" ><span>I'm</span> Onedibe Emmanuel</h1>""")
        self.assertContains(response, """I'm a Nigerian based Web & App developer focused on crafting clean & user‑friendly experiences, I am passionate about building excellent software that improves the lives of those around me.""")
        self.assertContains(response, """more about me""")

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Chat with me if interested .')