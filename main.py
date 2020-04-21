"""Final Project

Implement a Trie that will maintain strings it has already seen.
author: Danh Vo
date: 04/20/2020
version: 1.0
"""
print('Final Project CS 3345')


class Trie:
    def __init__(self, node):
        """
        Constructor
        """
        self.node = node
        print("Tried created")

    def insert(s: str):
        """
        Insert method
        """
        print("Insert ", s, " into this Trie")
        node = root
        for char in s:
            is_found = False
            # Search for the character in the children of the present `node`
            for child in node.children:
                if child.value == char:
                    # We found it, increase the counter by 1 to keep track that another
                    # word has it as well
                    child.count += 1
                    # And point the node to the child that contains this char
                    node = child
                    is_found = True
                    break
            # We did not find it so add a new chlid
            if not is_found:
                new_node = Node(char)
                node.children.append(new_node)
                # And then point node to the new child
                node = new_node
        # Everything finished. Mark it as the end of a word.
        node.word_finished = True

    def find(self, string):
        """
        Find method
        """
        print("Finding ", string, " in this Trie")

    def predict(self, string, n):
        """
        Predict method
        """
        print("predicting string: ", string, " with n = ", n)


class Node:
    def __init__(self, value, isEnd, count, children):
        self.value = value
        self.isEnd = isEnd
        self.count = count
        self.children = children
        print("Node created")


root = Node(1, True, 1, None)
trie = Trie(root)
trie.insert("String to insert")
trie.find("String to find")
trie.predict("String to predict", 2)