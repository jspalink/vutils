# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../../../src")

from unittest import TestCase
from vutils.output.vobject import VObject


class TestVObject(TestCase):
    
    def test_init(self):
        type = 'concept'
        text = 'This is my text here'
        sentence = 1
        o = VObject(type, text=text, sentence=sentence)
        self.assertEqual(type, o.type)
        self.assertEqual(text, o.text)
        self.assertEqual(sentence, o.sentence)
        self.assertTrue(o.object_category.is_empty)
    
    def test_as_dict(self):
        o = VObject('concept')
        expected = {
            'type': 'concept'
        }
        self.assertEqual(expected, o.as_dict())
        
        # add in two object_category objects
        o.object_category.add_object_category('Person', 0.855, 'person#Ronaldo')
        o.object_category.add_object_category('Place', 0.255, 'place#Chicago')
        expected = {
            'type': 'concept',
            'objectCategory': [
                {'class': 'Person', 'confidence': 0.855, '@id': 'person#Ronaldo'},
                {'class': 'Place', 'confidence': 0.255, '@id': 'place#Chicago'},
            ]
        }
        self.assertEqual(expected, o.as_dict())
