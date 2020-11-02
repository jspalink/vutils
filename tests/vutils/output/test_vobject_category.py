# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../../../src")

from unittest import TestCase
from vutils.output.vobject_category import VObjectCategory


class TestVObjectCategory(TestCase):
    
    def setUp(self):
        self.o = VObjectCategory()
    
    def test_add_object_category(self):
        self.o.add_object_category('Person')
        self.o.add_object_category('Place', 0.9881, 'spam_and_eggs')
        self.assertTrue('Person' in self.o.object_classes)
        self.assertTrue('Place' in self.o.object_classes)
        expected = {'class': 'Place', 'confidence': 0.9881, '@id': 'spam_and_eggs'}
        self.assertEqual(expected, self.o.object_category[1])
    
    def test_is_empty(self):
        self.assertTrue(self.o.is_empty)
        self.o.add_object_category('Place', 0.9881, 'spam_and_eggs')
        self.assertFalse(self.o.is_empty)
    
    def test_as_dict(self):
        self.o.add_object_category('Person')
        self.o.add_object_category('Place', 0.9881, 'spam_and_eggs')
        expected = [
            {'class': 'Person'},
            {'class': 'Place', 'confidence': 0.9881, '@id': 'spam_and_eggs'}
        ]
        self.assertEqual(expected, self.o.as_dict())
