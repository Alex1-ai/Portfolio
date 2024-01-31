
from .test_setup import TestSetup
# from ..models import About
class TestAboutViewTestCase(TestSetup):

    def test_about_page_status_code(self):
        response = self.client.get("/about")
        self.assertEquals(response.status_code, 200)

    def test_about_view_url_by_name(self):
        response = self.client.get(self.about_url)
        self.assertEquals(response.status_code, 200)

    def test_about_view_uses_correct_template(self):
        response = self.client.get(self.about_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')


#     def test_about_page_contains_correct_html(self):
#         response = self.client.get(self.about_url)
#         self.assertContains(response, """<h1>ABOUT <span>ME</span></h1>""")
#         # self.assertContains(response, """<h1>my <span>about</span></h1>""")
#         # self.assertContains(response, """more about me""")

#     def test_about_page_does_not_contain_incorrect_html(self):
#         response = self.client.get(self.about_url)
#         self.assertNotContains(
#             response, 'Chat with me if interested .')
        


# MODEL TEST
    # def test_portfolio_model_text_content(self):
    #     portfolio = Portfolio.objects.get(id=1)
    #     expected_object_title = f"{portfolio.title}"
    #     expected_object_langauge = f"{portfolio.langauge}"
    #     expected_object_link = f"{portfolio.link}"
    #     expected_object_client = f"{portfolio.client}"
    #     expected_object_project_type = f"{portfolio.project_type}"
    #     expected_object_image = f"{portfolio.image}"

    #     self.assertEquals(expected_object_title, "Test Portfolio")
    #     self.assertEquals(expected_object_langauge, "English")
    #     self.assertEquals(expected_object_link, "https://www.oce-markt.com")
    #     self.assertEquals(expected_object_client, "Freelance")
    #     self.assertEquals(expected_object_project_type, "Web Application")
    #     self.assertEquals(expected_object_image, "media/blog/softwareEngi.jpg")
    

    # # def test_portfolio_model_create_model(self):
    # #     response = self.client.post()
    # def test_portfolio_model_list_view(self):
    #     response = self.client.get(self.portfolio_url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'Test Portfolio')
    #     self.assertTemplateNotUsed(response, 'blog.html')


    
    # def test_blog_detail_page(self):
    #     response = self.client.get('/blog')
    #     self.assertEquals(response.status_code, 200 )

    