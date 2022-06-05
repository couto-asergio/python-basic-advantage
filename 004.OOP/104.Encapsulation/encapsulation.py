"""
Encapsulation

public, protected, private

# Python Conventions
    Protected Attribute
        _self._data = {}

    Private Attribute
    __self.data = {}

OBS.
    In python when the attributes has one or two
    underline, nobary can't to has access.
"""


class DateBase:
    def __init__(self):
        self.data = {}

    def add_client(self, id, name):
        if 'client' not in self.data:
            self.data['client'] = {id: name}
        else:
            self.data['client'].update({id: name})

    def list_client(self):
        for id, name in self.data['client'].items():
            print(id, name)

    def del_client(self):
        del self.data['client'][id]
