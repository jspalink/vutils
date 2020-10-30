

class VOutput(object):
    
    def __init__(self, validation_contracts=None):
        self.output = dict(
            validationContracts=validation_contracts,
            vendor=dict(api_calls=0)
        )
    
    def add_item(self, k, v):
        if k not in self.output:
            self.output[k] = []
        self.output[k].append(v)
    
    def set_api_calls(self, api_calls):
        self.output['vendor']['api_calls'] = api_calls
    
    def as_dict(self):
        output = dict()
        for k, v in self.output.items():
            if k not in {'validationContracts', 'vendor'}:
                if isinstance(v, (list,)):
                    try:
                        v = [t.as_dict() for t in v]
                    except:
                        pass
                else:
                    try:
                        v = v.as_dict()
                    except:
                        pass
            output[k] = v
        return output
