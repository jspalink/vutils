# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../../../src")

from unittest import TestCase
from vutils.input import parse_content
from vutils.input.sentence_word_collection import SentenceWordCollection


class TestInput(TestCase):
    
    def setUp(self):
        self.input_files = {
            'vtn': os.path.join(os.path.dirname(__file__), '../data/transcript.json'),
            'text': os.path.join(os.path.dirname(__file__), '../data/transcript.txt')
        }
    
    def test_parse_content(self):
        with open(self.input_files['vtn'], 'rb') as f:
            x = parse_content(f.read().decode('utf8'))
        self.assertIsInstance(x, SentenceWordCollection)
        self.assertTrue(x.has_timestamps)
        self.assertEqual(1305, len(list(x.yield_sentences())))
        self.assertEqual(x.sentences, list(x.yield_sentences()))
        last_sentence = "The presentation is pure media."
        self.assertEqual(last_sentence, x.sentences[-1].get_text())
    
    def test_get_sentence(self):
        with open(self.input_files['vtn'], 'rb') as f:
            x = parse_content(f.read().decode('utf8'))
        expected = x.sentences[100]
        self.assertEqual(expected, x.get_sentence(100))
    
    def test_yield_sentence_batches(self):
        with open(self.input_files['vtn'], 'rb') as f:
            x = parse_content(f.read().decode('utf8'))
        expected_lengths = [1000, 305]
        batches = list(x.yield_sentence_batches(1000))
        self.assertEqual(expected_lengths[0], len(batches[0]))
        self.assertEqual(expected_lengths[1], len(batches[1]))
    
    def test_yield_sentences(self):
        with open(self.input_files['vtn'], 'rb') as f:
            x = parse_content(f.read().decode('utf8'))
        expected = x.sentences
        x.sentences = None
        self.assertIsNone(x.sentences)
        self.assertEqual([a.get_text() for a in expected], [a.get_text() for a in x.yield_sentences()])
        self.assertIsNotNone(x.sentences)
        self.assertNotEqual(expected[0], x.sentences[0])
    
    def test_parse_content_plaintext(self):
        with open(self.input_files['text'], 'rb') as f:
            x = parse_content(f.read().decode('utf8'))
        self.assertIsInstance(x, SentenceWordCollection)
        self.assertFalse(x.has_timestamps)
        self.assertEqual(1301, len(list(x.yield_sentences())))
        self.assertEqual(x.sentences, list(x.yield_sentences()))
        last_sentence = "The presentation is pure media."
        self.assertEqual(last_sentence, x.sentences[-1].get_text())


