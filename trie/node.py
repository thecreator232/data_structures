__author__ = 'thecreator232'
from exceptions import ChildDoesNotExist


class Node(object):
    def __init__(self, parent, key, child=None, value=None):
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
        if self._child is not None:
            try:
                return self._child[key]
            except ChildDoesNotExist as e:
                raise e
        else:
            return None

    def get_parent(self):
        """Returns the parent of the current Node object."""
        return self._parent

    def get_path(self, parent=get_parent()):
        """ Gives the path of the current node with respect to the root of the trie.
        It backtracks the path by recursively calling the node's parent,
        until it reaches the root node.

        Params:
            parent: Takes an instance of Node type class.
        Retruns:
            Path of the node in string, with each key seperated by "/".
        """
        path = []
        if parent is not None:
            path.append(self.key)
            return self.get_path(parent=parent.get_parent())
        return "/".join(path.reverse())

    def get_value(self):
        """Returns the value associated with the object, if object contains
         no value, it returns NoneType Object.
         """
        return self._value

    def list_children(self):
        """ Returns list of children."""
        return self._child.keys()

    def insert_child(self, node):
        """Add's a new child of the current node.

        Params:
            node: Node type object.
        Returns:
            returns True if object is inserted, otherwise returns False.
        """
        try:
            self._child[node._key] = node
            return True
        except Exception:
            return False

class RootNode(Node):
    def __init__(self):
        super(RootNode, self).__init__(None, None)


class LeafNode(Node):
    def __init__(self, parent, value, key):
        super(LeafNode, self).__init__(parent, value, key)