import copy

class StdClass(object):
    """
    Class for giving dot access to a dictionary

    attrs:
        dictionary of attributes
        
    recursive:
        if True, attibutes of type dict will also have dot access
        as well dictionaries found in list attributes
    
    """

    def __init__(self, attrs={}, recursive=True):

        self.recursive = recursive

        for key, value in attrs.items():

            self.__classify(key, value)

    def _copy(self):
        """
        Underscore here prevents attributes of name 'copy' to override method
        """
        return copy.deepcopy(self)
        

    def __classify(self, key, value):
        """
        Set class attributes from dictionary keys
        """

        if self.recursive and isinstance(value, list):
            value = classify_list(value)
                    
        if not isinstance(value, dict) or not self.recursive:
            setattr(self, key, value)

        else:
            setattr(self, key, StdClass(value))
        

    def __getitem__(self, attribute):
        """
        Allow dict key access 
        """
        return getattr(self, attribute)

    def __setitem__(self, attribute, value):
        """
        Set attributes via dict key access
        """
        self.__classify(attribute, value)
            


def classify_list(_list, recursive=True):

    for i in range(len(_list)):
        if recursive and isinstance(_list[i], list):
            _list[i] = classify_list(_list[i])
        if isinstance(_list[i], dict):
            _list[i] = StdClass(_list[i], recursive)

    return _list
