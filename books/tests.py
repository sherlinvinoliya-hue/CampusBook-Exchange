from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from books.models import Book,Category
from .models import Favorite,ContactRequest
class InteractionTests(TestCase):
    def setUp(self):
        self.s=User.objects.create_user('seller',password='Pass12345!'); self.b=User.objects.create_user('buyer',password='Pass12345!'); c=Category.objects.create(name='General'); self.book=Book.objects.create(title='Book',author='Author',category=c,selling_price=100,seller=self.s)
        self.client.login(username='buyer',password='Pass12345!')
    def test_favorite_toggle_and_no_duplicate(self):
        self.client.post(reverse('toggle_favorite',args=[self.book.pk])); self.assertEqual(Favorite.objects.count(),1); self.client.post(reverse('toggle_favorite',args=[self.book.pk])); self.assertEqual(Favorite.objects.count(),0)
    def test_contact_seller(self):
        self.client.post(reverse('contact_seller',args=[self.book.pk]),{'message':'Interested','optional_contact':''}); self.assertTrue(ContactRequest.objects.filter(book=self.book,buyer=self.b,seller=self.s).exists())
