

class VSeries(object):
    
    def __init__(self, start_time_ms=None, stop_time_ms=None):
        self.start_time_ms = start_time_ms
        self.stop_time_ms = stop_time_ms
        self.data = dict()
    
    def set_data(self, key, value):
        self.data[key] = value
    
    def get_data(self, key):
        return self.data.get(key)
    
    def as_dict(self):
        d = {
            'startTimeMs': self.start_time_ms,
            'stopTimeMs': self.stop_time_ms
        }
        for k, v in self.data.items():
            try:
                v = v.as_dict()
            except:
                pass
            
            d[k] = v
        return d
