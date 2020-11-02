# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../../../src")

from unittest import TestCase
from vutils.output.vseries import VSeries


class TestVSeries(TestCase):
    
    def test_init(self):
        s = VSeries()
        self.assertIsNone(s.start_time_ms)
        self.assertIsNone(s.stop_time_ms)
        
        s = VSeries(100000, 100255)
        self.assertEqual(100000, s.start_time_ms)
        self.assertEqual(100255, s.stop_time_ms)
        
        self.assertEqual(dict(), s.data)
    
    def test_set_data(self):
        s = VSeries(100000, 100255)
        self.assertEqual(dict(), s.data)
        s.set_data('object', 'spam')
        self.assertTrue('object' in s.data)
        self.assertEqual('spam', s.data['object'])
        s.set_data('object', 'eggs')
        self.assertEqual('eggs', s.data['object'])
    
    def test_get_data(self):
        s = VSeries(100000, 100255)
        self.assertIsNone(s.get_data('object'))
        s.set_data('object', 'spam')
        self.assertEqual('spam', s.get_data('object'))
        s.set_data('object', 'eggs')
        self.assertEqual('eggs', s.get_data('object'))
    
    def test_as_dict(self):
        s = VSeries(100000, 100255)
        s.set_data('object', 'spam')
        expected = {
            'startTimeMs': 100000,
            'stopTimeMs': 100255,
            'object': 'spam'
        }
        self.assertEqual(expected, s.as_dict())
        
        class TestObject(object):
            def __init__(self, o):
                self.o = o
            
            def as_dict(self):
                return {
                    'o': self.o
                }
        
        s.set_data('object', TestObject('spam and eggs'))
        expected = {
            'startTimeMs': 100000,
            'stopTimeMs': 100255,
            'object': {'o': 'spam and eggs'}
        }
        self.assertEqual(expected, s.as_dict())
