from huffman import encode, decode


def test_huffman1():
    data = "abbaac"
    encoded, tree_root = encode(data)

    assert encoded == "011110010"
    assert decode(encoded, tree_root) == data


def test_huffman2():
    data = "The quick brown fox jumps over the lazy dog."
    encoded, tree_root = encode(data)

    assert decode(encoded, tree_root) == data


def test_huffman3():
    import requests

    wiki_page = requests.get("https://en.wikipedia.org/wiki/Huffman_coding")
    encoded, tree_root = encode(wiki_page.text)

    assert decode(encoded, tree_root) == wiki_page.text
