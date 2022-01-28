# https://leetcode.com/problems/design-add-and-search-words-data-structure/solution/
# Design Add and Search Words Data Structure
# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:
#
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false
# otherwise. word may contain dots '.' where dots can be matched with any letter.

'''
addWord()
We can design the datastructure to add and search word using Trie Datastructure
Trie can be initialised as nested hashmaps

** Another way to do it would be hashmap. But it is not the best version of solution because on adding more and more words might lead
to collisions.
Although this solution is not efficient for the most important practical use cases:
1. Finding all keys with a common prefix.
2. Enumerating a dataset of strings in lexicographical order.
3. Scaling for the large datasets. Once the hash table increases in size, there are a lot of hash collisions and the search time complexity could
 degrade to \mathcal{O}(N^2 \cdot M)O(N^2⋅M), where NN is the number of the inserted keys.
4. Trie could use less space compared to hashmap when storing many keys with the same prefix.
 In this case, using trie has only \mathcal{O}(M \cdot N)O(M⋅N) time complexity, where MM is the key length,
 and NN is the number of keys.
**

Searching a word:
 searching a word is easier using trie based on the common prefixes. However if we encounter a "." symbol the search needs to
 carried out for 26 characters. It runtime will be O(26^M).
'''


class Node:
    def __init__(self):
        self.keys = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for i, ch in enumerate(word):
            if ch not in node.keys:
                new_node = Node()
                node.keys[ch] = new_node
            node = node.keys[ch]
            #         terminating / end of word condition
            if i == len(word) - 1:
                node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root

        for i, ch in enumerate(word):
            # if '.' is encountered
            if ch not in node.keys:
                if ch == '.':
                    print("in if IS word=", node.isWord)
                    if node.isWord == False and self.search(self, word[i + 1:]):
                        return True
                return False
            else:
                node = node.keys[ch]
            print("IS word=", node.isWord)
        return node.isWord

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
word ="world"
obj.addWord(word)
param_2 = obj.search(word)
print(param_2)
