from django.test import TestCase
from django.urls import resolve, reverse


class LostFoundURLsTest(TestCase):
    def test_core_routes_resolve(self):
        self.assertEqual(resolve('/').func.__name__, 'landingpage')
        self.assertEqual(resolve('/dashboard/').func.__name__, 'dashboard')
        self.assertEqual(resolve('/items/').func.__name__, 'item_list')
        self.assertEqual(reverse('landingpage'), '/')
        self.assertEqual(reverse('dashboard'), '/dashboard/')
        self.assertEqual(reverse('item_list'), '/items/')
