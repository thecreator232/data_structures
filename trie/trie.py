__author__ = 'thecreator232'
from node import Node, RootNode
from meta import TrieMeta


class Trie(object):
    root = RootNode()
    meta = TrieMeta()

    def __init__(self, **kwargs):

    def add(self, key, value):
        node = self.root
        for xkey in key:
            if key in node.list_children():
                node = node.get_child(key=xkey)
            else:
                new_node = Node(node, xkey)
                node.insert_child(new_node)
        node.insert_value(value)

    def remove(self, key, value):
        pass

    def update(self, key, value):
        pass

    def key_exists(self, key):
        pass