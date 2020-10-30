from .vobject_category import VObjectCategory


class VObject(object):
    
    def __init__(self, type, text=None, label=None, sentence=None, *args, **kwargs):
        self.type = type
        self.text = text
        self.label = label
        self.sentence = sentence
        self.object_category = VObjectCategory()
    
    def as_dict(self):
        r = dict(type=self.type)
        if self.text is not None:
            r['text'] = self.text
        if self.label is not None:
            r['label'] = self.label
        if self.sentence is not None:
            r['sentence'] = self.sentence
        if self.object_category:
            r['objectCategory'] = self.object_category.as_dict()
        return r

