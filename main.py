"""Final Project

Implement a Trie that will maintain strings it has already seen.
author: Danh Vo
date: 04/20/2020
version: 1.0
"""
print('Final Project CS 3345')


class TrieNode:

    # Trie node class
    def __init__(self):
        self.value = None
        self.children = [None] * 26
        self.isEnd = False
        self.count = 0


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        root = self.root
        length = len(key)
        for level in range(length):
            index = (ord(key[level]) - ord('a'))

            # if current character is not present
            if not root.children[index]:
                root.children[index] = TrieNode()

            root.count += 1
            root.value = ord(key[level])
            root = root.children[index]

        # mark last node as leaf
        root.isEnd = True


    def find(self, key):

        # Search key in the trie
        # Returns true if key presents and false otherwise
        root = self.root
        length = len(key)
        for level in range(length):
            index = (ord(key[level]) - ord('a'))
            if not root.children[index]:
                return False
            root = root.children[index]

        return root != None and root.isEnd

    def predict(self, key, num):
        # Prediction
        return "Predicted"

def printWord(str, level):


    print('\n')
    for i in range(level):
        if str[level]:
            print(chr(str[i]), end="")


def printAllWords(root, wArray, level=0):
    if not root:
        return
    if root.isEnd:
        printWord(wArray, level)
    for i in range(26):
        if root.children[i]:
            wArray[level] = i + ord('a')
            printAllWords(root.children[i], wArray, level + 1)

if __name__ == "__main__":

    trie = Trie()

    words = [
        'test', 'apple', 'tester', 'ten', 'testing', 'tennant', 'tenure', 'tenacity', 'tentacle', 'tenantry',
        'tendency', 'tent', 'tenor', 'tend', 'tenders', 'tend', 'tending', 'tender', 'test', 'test', 'test',
        'quarintine', 'quaffle', 'quarrel', 'quirrell', 'quirrell', 'quirrell', 'quirrell', 'quaffle', 'quaffle',
        'quaffle', 'quaffle', 'quarintine',
    ]

    for word in words:
        trie.insert(word)

    level = 0
    str = [None]*20
    print("Content: ")
    printAllWords(trie.root, str)

    #
    # print(trie.predict('te', 2))  # returns ['test', 'tend']
    # print(trie.predict('qu', 3))  # returns ['quaffle', 'quirrell', 'quarintine']