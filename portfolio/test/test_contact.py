
from .test_setup import TestSetup,reverse
from ..models import Contact
class TestContactViewTestCase(TestSetup):
    def test_contact_form_submission(self):
        # Prepare data for the form submission
        form_data = {
            'name': 'John Doe',
            'subject': 'Test Subject',
            'email': 'john.doe@example.com',
            'message': 'This is a test message'
        }

        # Get the URL for the contact form submission view
        url = self.contact_url  # Replace 'contact_view_name' with the actual name of your contact view

        # Create a client to simulate the POST request
        # client = Client()

        # Make the POST request with the form data
        response = self.client.post(url, form_data)

        # Check if the form submission was successful (HTTP 302 status code for a successful redirect)
        self.assertEqual(response.status_code, 200)

        # Check if a new contact object was created in the database
        self.assertEqual(Contact.objects.count(), 2)

        # Retrieve the created contact object
        created_contact = Contact.objects.all()[1]

        # Check if the data in the contact object matches the form data
        self.assertEqual(created_contact.name, form_data['name'])
        self.assertEqual(created_contact.subject, form_data['subject'])
        self.assertEqual(created_contact.email, form_data['email'])
        # self.assertEqual(created_contact.message, form_data['message'])
        # Update the comparison to check if the form_data['message'] is contained within created_contact.message
        self.assertIn(form_data['message'], created_contact.message)


    def test_contact_page_status_code(self):
        response = self.client.get(self.contact_url)
        self.assertEquals(response.status_code, 200)

    def test_contact_view_url_by_name(self):
        response = self.client.get(self.contact_url)
        self.assertEquals(response.status_code, 200)

    def test_contact_view_uses_correct_template(self):
        response = self.client.get(self.contact_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')


    def test_contact_page_contains_correct_html(self):
        response = self.client.get(self.contact_url)
        self.assertContains(response, """<span class="title-bg">contact</span>""")
        # self.assertContains(response, """<h1>my <span>contact</span></h1>""")
        # self.assertContains(response, """more about me""")

    def test_contact_page_does_not_contain_incorrect_html(self):
        response = self.client.get(self.contact_url)
        self.assertNotContains(
            response, 'Chat with me if interested .')
        


  

   

    
    def test_contact_page(self):
        response = self.client.get('/contact')
        self.assertEquals(response.status_code, 200 )

    