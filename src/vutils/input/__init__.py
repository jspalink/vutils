from collections import namedtuple
from textblob import TextBlob
from nltk.tokenize import TweetTokenizer
from .sentence_word_collection import SentenceWordCollection

tokenizer = TweetTokenizer()
SentenceWord = namedtuple('SentenceWord', ['word', 'start_time_ms', 'stop_time_ms', 'start_offset', 'sentence_index', 'is_punctuation', 'is_sentence_ender'])


def parse_content_to_sentence_words(record):
    sentence_words = SentenceWordCollection()
    sentence_index = 0
    start_offset = 0
    for s in record.get('series', []):
        words = s.get('words', [])
        if len(words) > 0:
            w = words[0]
            is_punctuation = w.get('word') in ('.', '?', ',', ';', ':', '-', '—', '_', '@', '/', "'", '"')
            is_sentence_ender = w.get('word') in ('.', '?', '!')
            if start_offset > 0 and not is_punctuation:
                start_offset += 1
            
            word = SentenceWord(w.get('word'), s.get('startTimeMs'), s.get('stopTimeMs'), start_offset, sentence_index, is_punctuation, is_sentence_ender)
            sentence_words.add_sentence_word(word)
            start_offset += len(word.word)
            if is_sentence_ender:
                start_offset = 0
                sentence_index += 1
    x = list(sentence_words.yield_sentences())
    return sentence_words


def parse_plaintext_to_sentence_words(content):
    text = content.replace("\n", " ")
    textblob = TextBlob(text)
    sentence_index = 0
    sentence_words = SentenceWordCollection()
    for i, sentence in enumerate(textblob.sentences):
        start_offset = 0
        for token in tokenizer.tokenize(sentence.string):
            is_punctuation = token in ('.', '?', ',', ';', ':', '-', '—', '_', '@', '/', "'", '"')
            is_sentence_ender = token in ('.', '?', '!')
            if start_offset > 0 and not is_punctuation:
                start_offset += 1
            word = SentenceWord(token, None, None, start_offset, sentence_index, is_punctuation, is_sentence_ender)
            sentence_words.add_sentence_word(word)
            start_offset += len(word.word)
        sentence_index += 1
    x = list(sentence_words.yield_sentences())
    return sentence_words


def get_sentence_string(sentence_words):
    words = []
    for w in sentence_words:
        if w.start_offset != 0 and not w.is_punctuation:
            words.append(" ")
        words.append(w.word)
    return ''.join(words)