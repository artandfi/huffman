from heapq import heappop, heappush
from collections import Counter


class HuffmanTreeNode:
    def __init__(self, freq, char=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq
    
    @property
    def is_leaf(self):
        return not self.left and not self.right


def encode(data):
    tree_root = _make_tree(data)
    mapping = _make_mapping(tree_root)

    return "".join(mapping[char] for char in data), tree_root


def decode(data, tree_root):
    node = tree_root
    decoded = ""

    i = 0
    while i < len(data):
        while not node.is_leaf:
            node = node.left if data[i] == "0" else node.right
            i += 1
        
        decoded += node.char
        node = tree_root
    
    return decoded


def _make_tree(data):
    counter = Counter(data)
    chars_freqs = sorted(counter.items(), key=lambda x: (x[1], x[0]))
    nodes = []
    
    for char, freq in chars_freqs:
        heappush(nodes, HuffmanTreeNode(freq, char))
    
    while len(nodes) > 1:
        left = heappop(nodes)
        right = heappop(nodes)
        heappush(nodes, HuffmanTreeNode(left.freq+right.freq, left=left, right=right))
    
    return nodes[0]


def _make_mapping(node, mapping=None, bits="", value=""):
    if mapping is None:
        mapping = {}
    
    bits += value

    if node.left:
        _make_mapping(node.left, mapping, bits, "0")
    if node.right:
        _make_mapping(node.right, mapping, bits, "1")
    
    if node.is_leaf:
        mapping[node.char] = bits
    
    return mapping
