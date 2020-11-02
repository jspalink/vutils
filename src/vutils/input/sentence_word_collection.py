from .sentence import Sentence
import logging
log = logging.getLogger('main')


class SentenceWordCollection(object):
    """
    Provides an indexed sentence and word object that can be used to tie in timestamps
    """
    __slots__ = ['sentence_words', 'iterator', 'current_word', 'has_timestamps', 'sentences']
    
    def __init__(self, sentence_words=None, *args, **kwargs):
        if sentence_words:
            self.sentence_words = sentence_words
        else:
            self.sentence_words = []
        self.iterator = None
        self.current_word = None
        self.has_timestamps = False
        self.sentences = list()
    
    def add_sentence_word(self, sentence_word):
        """
        Add a SentenceWord object to our collection

        :param sentence_word:
        :return:
        """
        if not self.has_timestamps and sentence_word.start_time_ms is not None and sentence_word.stop_time_ms is not None:
            self.has_timestamps = True
        self.sentence_words.append(sentence_word)
    
    def find_next(self, sentence_index=0, offset=0, ending_offset=0):
        """
        return the next SentenceWord with an offset greater than or
        equal to offset. Leave the iterator where it was last.

        @param offset:
        @return:
        """
        words = []
        if not self.iterator or sentence_index < self.current_word.sentence_index:
            self.iterator = (x for x in self.sentence_words)
            self.current_word = next(self.iterator)
        
        while True:
            start_offset = self.current_word.start_offset
            end_offset = len(self.current_word) + self.current_word.start_offset
            if self.current_word.sentence_index == sentence_index and offset <= start_offset < ending_offset:
                words.append(self.current_word)
            
            if self.current_word.sentence_index >= sentence_index and start_offset >= ending_offset:
                break
            
            try:
                self.current_word = next(self.iterator)
            except StopIteration as e:
                log.debug("StopIteration during find_next...")
                break
        
        return words
    
    def get_sentence(self, sentence_index):
        """
        Return a particular sentence

        @param sentence_index:
        @return:
        """
        if not self.sentences:
            self.sentences = list(self.yield_sentences())
        return self.sentences[sentence_index]
    
    def yield_sentences(self):
        """
        posts = [x[4] for x in sentences]
        posts_lengths = [ceil(len(x) / 2000) for x in posts]
        timestamps = [(x[0], x[1]) for x in sentences]

        Provides, essentially, posts, post_lengths, and timestamps

        @return:
        """
        if self.sentences:
            for s in self.sentences:
                yield s
            return
        
        self.sentences = list()
        sentence = Sentence()
        sentence_index = 0
        iterator = (x for x in self.sentence_words)
        while True:
            try:
                current_word = next(iterator)
                if current_word.sentence_index > sentence_index:
                    yield sentence
                    self.sentences.append(sentence)
                    sentence_index += 1
                    sentence = Sentence()
                sentence.sentence_words.append(current_word)
            
            except Exception as e:
                if sentence:
                    yield sentence
                    self.sentences.append(sentence)
                break
        return
    
    def yield_sentence_batches(self, batch_size=100):
        """
        Return a generator of batches of _n_ sentences

        :param n:
        :return:
        """
        sentences = list(self.yield_sentences())
        num_sentences = len(sentences)
        for x in range(0, num_sentences, batch_size):
            yield sentences[x:min(x + batch_size, num_sentences)]
    
    def get_full_text(self, separator=' '):
        """
        Return the full text of the SentenceWords
        :return:
        """
        return separator.join((s.get_text() for s in self.yield_sentences()))
