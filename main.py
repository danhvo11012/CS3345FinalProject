"""Final Project CS3345

Implement a Trie that will maintain strings it has already seen.
The Project file contains only two classes: Trie and TrieNode

author: Danh Vo
date: 04/24/2020
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
    #---------------------------------------------------------------------------------------------------
    #
    #
    #                                       PUBLIC METHODS
    #
    #
    #---------------------------------------------------------------------------------------------------

    def __init__(self):
        """
        Constructor
        """
        self.root = TrieNode()

    def insert(self, key):
        """
        Insertion method

        Insert key into the trie
        """
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
        """
        Finding method

        Search key in the trie
        Returns true if key presents and false otherwise
        """
        root = self.root
        length = len(key)
        for level in range(length):
            index = (ord(key[level]) - ord('a'))
            if not root.children[index]:
                return False
            root = root.children[index]
        return root != None and root.isEnd

    def predict(self, word, n):
        """
        Use a partial word to find the top n likely words this word could be
        """
        return(self.__dfs(word, self.root, word, n))

    #---------------------------------------------------------------------------------------------------
    #
    #
    #                                       PRIVATE METHODS
    #
    #
    #---------------------------------------------------------------------------------------------------

    def __getWord(self, preFix, wList, str, level):
        """
        Return a complete word from root.
        """
        word = ""
        word += preFix
        for i in range(level):
            word += chr(str[i])
        wList.append(word)


    def __getAllWords(self, parentValue, wList, root, wordArray, level=0):
        """
        Recursively retrieve all possible words starting at the search value
        """
        if not root:
            return None

        if root.isEnd:
            preFix = root.count
            self.__getWord(str(preFix) + parentValue, wList, wordArray, level)

        for i in range(26):
            if root.children[i]:
                wordArray[level] = i + ord('a')
                self.__getAllWords(parentValue, wList, root.children[i], wordArray, level + 1)

    def __countCmp(self, e):
        """
        Sorting helper function
        """
        return e.count

    def __getNPossibleWords(self, prefix, root, n):
        """
        Get n most occured words based on input
        """
        nodeList = []
        for child in root.children:
            if child:
                nodeList.append(child)

        # Sort child List based on word count
        nodeList.sort(reverse=True, key=self.__countCmp)

        # Get all possible words from each child
        wordArray = [None] * 20
        wordList = []
        for node in nodeList:
            self.__getAllWords(prefix + node.value, wordList, node, wordArray)

        # Sort results based on its prefix number
        wordList.sort(reverse=True)

        # Remove prefix number from results
        result = wordList[0:n]
        for index, resultWord in enumerate(result):
            result[index] = resultWord[1:]

        return result

    def __dfs(self, prefix, root, word, n, res=[],):
        """
        Depth-first search implementation
        """
        for neighbour in root.children:
            if neighbour and neighbour.value == word[0]:
                if len(word) == 1:
                    # Get the node associates with searh key, they find n most occured words from there.
                    return self.__getNPossibleWords(prefix, neighbour, n)
                else:
                    return self.__dfs(prefix, neighbour, word[1:], n, res)

        return res


# Main function for testing purposes
if __name__ == "__main__":

    trie = Trie()

    words = [
        'test',
        'apple', 'tester', 'ten', 'testing', 'tennant', 'tenure', 'tenacity', 'tentacle', 'tenantry',
        'tendency', 'tent', 'tenor', 'tend', 'tenders', 'tend', 'tending', 'tender', 'test', 'test', 'test',
        'quarintine', 'quaffle', 'quarrel', 'quirrell', 'quirrell', 'quirrell', 'quirrell', 'quaffle', 'quaffle',
        'quaffle', 'quaffle', 'quarintine',
    ]

    for word in words:
        trie.insert(word)

    print(trie.predict('te', 2))  # returns ['test', 'tend']
    print(trie.predict('qu', 3))  # returns ['quaffle', 'quirrell', 'quarintine']
