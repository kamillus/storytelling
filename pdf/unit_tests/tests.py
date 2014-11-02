from django.test import TestCase
from datetime import datetime, timedelta
from pdf.models import *
from django.contrib.auth.models import User
from django.utils.html import escape
from django.contrib.auth import login
from django.test.client import RequestFactory

class HomePageTest(TestCase):
    
    def test_home_redirects_to_enter(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/enter/', status_code=302, target_status_code=200)   
    
    def test_enter_renders_correct_template(self):
        response = self.client.get('/enter/')
        self.assertTemplateUsed(response, 'access_code_form.html')
        
    def test_enter_renders_error_when_empty(self):
        response = self.client.post('/enter/', data={'access_code': ''})
        self.assertContains(response, escape("This field is required"))
        
    def test_enter_invalid_code(self):
        response = self.client.post('/enter/', data={'access_code': 'CODE'})
        self.assertContains(response, escape("Invalid access code"))
    
    def test_enter_code_not_accessible(self):
        user = User.objects.create(username='test_user')
        #UserProfile.objects.create(user=user)
        
        access_code = AccessCode(code="ABC", date_of_release= datetime.now()+timedelta(days=30), user=user)
        access_code.save()
        
        response = self.client.post('/enter/', data={'access_code': 'ABC'})
        self.assertContains(response, escape("Access code not available at this time"))
        
    def test_enter_code_is_valid_redirect(self):
        user = User.objects.create(username='test_user')
        access_code = AccessCode(code="ABC", date_of_release= datetime.now()-timedelta(days=30), user=user)
        access_code.save()
        
        response = self.client.post('/enter/', data={'access_code': 'ABC'})
        self.assertRedirects(response, '/console', status_code=302, target_status_code=301)
        
class ConsoleTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='test_user')
        access_code = AccessCode(code="ABC", date_of_release= datetime.now()-timedelta(days=30), user=user)
        access_code.save()
        response = self.client.post('/enter/', data={'access_code': 'ABC'})
    
    def test_console_renders_correct_template(self):
        response = self.client.get('/console/')
        self.assertTemplateUsed(response, 'console.html')
        
    def test_book_detail_renders_correct_template(self):
        response = self.client.get('/book/1/')
        self.assertTemplateUsed(response, 'book_detail.html')