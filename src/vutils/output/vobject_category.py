class VObjectCategory(object):
    
    def __init__(self):
        self.object_category = []
        self.object_classes = set()
    
    @property
    def is_empty(self):
        return len(self.object_category) == 0
    
    def add_object_category(self, object_class, object_confidence=None, object_id=None, *args, **kwargs):
        if object_class not in self.object_classes:
            o = {'class': object_class}
            if object_confidence:
                o['confidence'] = object_confidence
            if object_id:
                o['@id'] = object_id
            self.object_category.append(o)
            self.object_classes.add(object_class)
    
    def as_dict(self):
        return self.object_category