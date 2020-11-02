import logging
log = logging.getLogger('main')


class Sentence(object):
    """
    A collection of SentenceWord objects that are representative of a single sentence
    """
    
    def __init__(self, sentence_words=None):
        """
        
        :param sentence_words: A list of SentenceWord namedtuples
        """
        self.sentence_words = sentence_words
        if not self.sentence_words:
            self.sentence_words = []
        self.annotations = dict()
    
    @property
    def start_time_ms(self):
        return self.sentence_words[0].start_time_ms
    
    @property
    def stop_time_ms(self):
        return self.sentence_words[-1].stop_time_ms
    
    @property
    def sentence_index(self):
        return self.sentence_words[0].sentence_index
    
    def get_text(self):
        words = []
        for w in self.sentence_words:
            if w.start_offset != 0 and not w.is_punctuation:
                words.append(" ")
            words.append(w.word)
        return ''.join(words)




