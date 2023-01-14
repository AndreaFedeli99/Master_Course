# Python's dictionaries do not preserve the order of inserted data nor store the data sorted by the key.
# Write an extension for the dict class whose instances will keep the data sorted by their key value.
# Note that the order must be preserved also when new elements are added.

class OrderedDict(dict):
    __keys_list = []

    def __init__(self, args):
        [self.__insert_key(k) for k in args]
        super().__init__(args)

    __is_str = lambda self, s: "'"+s+"'" if type(s) == str else s
    __insert_key = lambda self, __key: \
                    ( \
                        # if __keys_list is empty => append the first element to the list of keys
                        len(self.__keys_list) == 0 and (self.__keys_list.append(__key) or True)
                    ) or \
                    ( \
                        # if the key to insert is not the biggest => insert the element at the correct position
                        len([i for i,e in enumerate(self.__keys_list, 0) if str(__key) < str(e)]) != 0 and \
                        (self.__keys_list.insert([i for i,e in enumerate(self.__keys_list, 0) if str(__key) < str(e)][0], __key) or True)
                    ) or \
                    (
                        # the key to insert is the biggest => append the element
                        self.__keys_list.append(__key)
                    )
                                    
    def __setitem__(self, __key, __value):
        self.__insert_key(__key)
        return super().__setitem__(__key, __value)

    def __str__(self):
        return '{' + ', '.join([i for i in list(map(lambda k : f'''{self.__is_str(k)}:{self.__is_str(self[k])}''', [k for k in self.__keys_list]))]) + '}'

od = OrderedDict({'2': 'two', '4': 'one', '3': 'three'})
print(od)

od['5'] = 'five'
od['1'] = 'one'
print(od)