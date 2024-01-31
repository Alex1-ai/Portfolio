from django.http import HttpRequest
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from portfolio import views

class BlogPageTests(TestCase):

    def test_blog_page_status_code(self):
        response = self.client.get('/blog')
        self.assertEquals(response.status_code, 200)

    def test_blog_view_url_by_name(self):
        response = self.client.get(reverse('blog'))
        self.assertEquals(response.status_code, 200)
    

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blog'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog.html')


    def test_blog_page_contains_correct_html(self):
        response = self.client.get('/blog')
        self.assertContains(response, '<h1>my <span>blog</span></h1>')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there ')
        
