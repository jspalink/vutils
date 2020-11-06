from .vobject_category import VObjectCategory


class VObject(object):
    
    def __init__(self, type, text=None, label=None, sentence=None, data=None, *args, **kwargs):
        self.type = type
        self.text = text
        self.label = label
        self.sentence = sentence
        self.object_category = VObjectCategory()
        self.data = data or dict()
    
    def as_dict(self):
        r = dict(type=self.type)
        if self.text is not None:
            r['text'] = self.text
        if self.label is not None:
            r['label'] = self.label
        if self.sentence is not None:
            r['sentence'] = self.sentence
        if not self.object_category.is_empty:
            r['objectCategory'] = self.object_category.as_dict()
        for k, v in self.data.items():
            if hasattr(v, 'as_dict'):
                v = v.as_dict()
            r[k] = v
        return r

