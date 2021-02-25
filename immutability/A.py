class A: 
    def __init__(self, name):    
        self.__dict__['name'] = name 
    def __setattr__(self, name, value):
        if name == 'name':
            raise ValueError('Not Allowed')

