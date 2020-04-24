"""Final Project CS3345

Implement a Trie that will maintain strings it has already seen.
The Project file contains only two classes: Trie and TrieNode

author: Danh Vo
date: 04/20/2020
version: 1.0
"""


class TrieNode:
    """
    Class TrieNode. Blueprint of a Trie's node
    """
    def __init__(self):
        self.value = None
        self.children = [None] * 26
        self.isEnd = False
        self.count = 0


class Trie:
    """
    Class Trie. Skeleton of the Trie class
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):

        root = self.root
        length = len(key)

        for level in range(length):
            index = (ord(key[level]) - ord('a'))

            if not root.children[index]:
                root.children[index] = TrieNode()

            root = root.children[index]
            root.value = key[level]

        root.count += 1
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

    # Helper functions to display the Trie content from a node
    def getWord(self, preFix, wList, str, level):
        word = ""
        word += preFix
        for i in range(level):
            word += chr(str[i])
        wList.append(word)

    def getAllWords(self, parentValue, wList, root, wordArray, level=0):
        if not root:
            return None

        if root.isEnd:
            preFix = root.count
            self.getWord(str(preFix) + parentValue, wList, wordArray, level)

        for i in range(26):
            if root.children[i]:
                wordArray[level] = i + ord('a')
                self.getAllWords(parentValue, wList, root.children[i], wordArray, level + 1)

    def countCmp(self, e):
        """
        Sorting helper function
        """
        return e.count

    def getNPossibleWords(self, res, prefix, root, n):

        nodeList = []
        for child in root.children:
            if child:
                nodeList.append(child)

        # Sort child List based on word count
        nodeList.sort(reverse=True, key=self.countCmp)

        wordArray = [None] * 20
        wordList = []

        # Display sorted child list
        for node in nodeList:
            # print(node.value, node.count)
            self.getAllWords(prefix + node.value, wordList, node, wordArray)

        wordList.sort(reverse=True)
        rawResult = wordList[0:n]
        for index, resultWord in enumerate(rawResult):
            rawResult[index] = resultWord[1:]

        res = rawResult[:]

        return res

    def dfs(self, prefix, root, word, n, res=[],):

        for neighbour in root.children:

            if neighbour:
                neighbour.count += 1

                if neighbour.value == word[0]:
                    if len(word) == 1:
                        return self.getNPossibleWords(res, prefix, neighbour, n)

                    else:
                        return self.dfs(prefix, neighbour, word[1:], n, res)

        return res

    def predict(self, word, n):
        return(self.dfs(word, self.root, word, n))


# Main function for testing purposes
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


    print(trie.predict('te', 2))  # returns ['test', 'tend']
    print(trie.predict('qu', 3))  # returns ['quaffle', 'quirrell', 'quarintine']