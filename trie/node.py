__author__ = 'thecreator232'


class Node(object):
    def __init__(self, parent, key, value=None, child=None):
        self._value = value
        self._key = key
        self._child = child
        self._parent = parent


    def get_child(self, key):
        """
        returns the child Node object with the specified key.

        Params:
            key: string

        Returns:
            Node object. If child does not exist a NoneType object
            will be returned.
        """
        pass

    def get_parent(self):
        """Returns the parent of the current Node object."""
        return self._parent

    def get_path(self):
        pass

    def get_value(self):
        """Returns the value associated with the object, if object contains
         no value, it returns NoneType Object.
         """
        pass

    def list_children(self):
        """ Returns list of children."""
        pass

class RootNode(Node):
    def __init__(self):
        super(RootNode, self).__init__(None, None)


class LeafNode(Node):
    def __init__(self, parent, value, key):
        super(LeafNode, self).__init__(parent, value, key)