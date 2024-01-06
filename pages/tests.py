from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.

class HomePageTest(SimpleTestCase):
    def test_url_exist_location(self):
        response=self.client.get("/")
        self.assertEqual(response.status_code,200) 

    def test_url_available_by_name(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_correct_template_name(self):
        response=self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    
class AboutPageTest(SimpleTestCase):
    def test_url_exit_location(self):
        response=self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response=self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
    
    def test_correct_template_name(self):
        response=self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")
