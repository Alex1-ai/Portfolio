# from django.http import HttpRequest
from django.test import  TestCase
from django.urls import reverse
from blog.models import Blog
# from portfolio import views
# from faker import Faker

class BlogModelTestCase(TestCase):

    def setUp(self):
        # faker = Faker()
        Blog.objects.create(
            title = "Test title",
            content = "This is a test content just testing it making sure it works",
            tags = "#Programmers #Software Developer",
            author = "Alex1.ai",
            image = "media/blog/softwareEngi.jpg"
        )

    def test_blog_model_text_content(self):
        blog = Blog.objects.get(id=1)
        expected_object_title = f"{blog.title}"
        expected_object_content = f"{blog.content}"
        expected_object_tags = f"{blog.tags}"
        expected_object_author = f"{blog.author}"
        expected_object_image = f"{blog.image}"

        self.assertEquals(expected_object_title, "Test title")
        self.assertEquals(expected_object_content, "This is a test content just testing it making sure it works")
        self.assertEquals(expected_object_tags, "#Programmers #Software Developer")
        self.assertEquals(expected_object_author, "Alex1.ai")
        self.assertEquals(expected_object_image, "media/blog/softwareEngi.jpg")

    def test_blog_model_list_view(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test title')
        self.assertTemplateUsed(response, 'blog.html')


    
    def test_blog_detail_page(self):
        response = self.client.get('/blog-detail/1')
        self.assertEquals(response.status_code, 200 )

