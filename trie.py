class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.is_word_end = False

class Trie:

    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, ch):

        # Converts key current character into index
        # use only 'a' through 'z' and lower case
        return ord(ch) - ord('a')

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        curr = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            if not curr.children[index]:
                curr.children[index] = self.getNode()
            curr = curr.children[index]

            # mark last node as leaf
        curr.is_word_end = True

    def search(self, key):

        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        curr = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not curr.children[index]:
                return False, False
            curr = curr.children[index]

        return curr != None, curr.is_word_end