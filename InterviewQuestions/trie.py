class Node:
    def __init__(self):
        self.keys = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insertWord(self, word):
        node = self.root
        for i, ch in enumerate(word):
            if ch not in node.keys:
                newNode = Node()
                node.keys[ch] = newNode
            node = node.keys[ch]
            if i == len(word) - 1:
                node.isWord = True

    def searchWord(self, word):
        node = self.root
        for ch in word:
            if ch not in node.keys:
                return False
            node = node.keys[ch]
        return node.isWord

trie = Trie()
wordList = ['hello', 'world', 'my', 'name', 'is', 'mocha']
for word in wordList:
    trie.insertWord(word)
    print("{} present? {}".format(word, trie.searchWord(word)))
negList = ['i', 'am','helloworld', 'milk', 'mocha']
for word in negList:
    print("{} present? {}".format(word, trie.searchWord(word)))
