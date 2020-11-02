# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../../../src")

from unittest import TestCase
from vutils.output.voutput import VOutput
from vutils.output.vseries import VSeries


class TestVOutput(TestCase):
    
    def setUp(self):
        self.o = VOutput(['concept'])
        self.sa = VSeries(100000, 100255)
        self.sb = VSeries(100256, 123312)
        self.sc = VSeries(123313, 163312)
    
    def test_add_item(self):
        self.assertIsNone(self.o.output.get('series'))
        self.assertEqual(2, len(self.o.output))
        self.assertFalse('series' in self.o.output)
        self.o.add_item('series', self.sa)
        self.assertEqual(1, len(self.o.output.get('series')))
        self.o.add_item('series', self.sb)
        self.assertEqual(2, len(self.o.output.get('series')))
        self.o.add_item('series', self.sc)
        self.assertEqual(3, len(self.o.output.get('series')))
    
    def test_set_api_calls(self):
        self.assertEqual(0, self.o.output['vendor']['api_calls'])
        self.o.set_api_calls(100)
        self.assertEqual(100, self.o.output['vendor']['api_calls'])
        self.o.set_api_calls(254)
        self.assertEqual(254, self.o.output['vendor']['api_calls'])
    
    def test_as_dict(self):
        self.o.add_item('series', self.sa)
        self.o.add_item('series', self.sb)
        self.o.add_item('series', self.sc)
        expected = {
            'validationContracts': ['concept'],
            'vendor': {'api_calls': 0},
            'series': [
                {
                    "startTimeMs": 100000,
                    "stopTimeMs": 100255
                },
                {
                    "startTimeMs": 100256,
                    "stopTimeMs": 123312
                },
                {
                    "startTimeMs": 123313,
                    "stopTimeMs": 163312
                }
            ]
        }
        self.assertEqual(expected, self.o.as_dict())
    
