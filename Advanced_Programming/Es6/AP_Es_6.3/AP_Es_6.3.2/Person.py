
class Person():
    def __init__(self, name, lastname, birthday):
        self._name = name
        self._lastname = lastname
        self._birthday = birthday
    
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
    
    def get_lastname(self):
        return self._lastname
    
    def set_lastname(self, lastname):
        self._lastname = lastname
    
    def get_birthday(self):
        return self._birthday

    def set_birthday(self, birthday):
        self._birthday = birthday

    def __repr__(self):
        return self._name + ' ' + self._lastname + ', ' + str(self._birthday)