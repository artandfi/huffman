from huffman import encode, decode


def main():
    print("---Huffman coding demo by (c)artandfi---")

    while True:
        data = input("Enter the message to be encoded: ")
        encoded, tree_root = encode(data)

        print(f"Encoded data: {encoded}")
        print(f"Decoded data: {decode(encoded, tree_root)}")
        print("---------")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        quit()
