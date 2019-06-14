class TrieNode:

    def __init__(self):
        '''
        Init trie node, with 26 char space.
        '''
        self.children = [None] * 26
        self.is_word_end = False

class Trie:

    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, ch):
        '''
        Converts current character into index use only 'a' through 'z' and lower case
        :param ch:
        :return:
        '''
        return ord(ch) - ord('a')

    def insert(self, key):
        '''
        If not present, inserts key into trie. If the key is prefix of trie node, just marks leaf node as a word.
        :param key:
        :return:
        '''
        curr = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            if not curr.children[index]:
                curr.children[index] = self.getNode()
            curr = curr.children[index]

        # mark last node as leaf, i.e., a word.
        curr.is_word_end = True

    def search(self, key):
        '''
        Search key in the trie. Returns true if key presents in trie, else false.
        Need to tell caller whether it's reaching the end, as well as whether it's a word.
        :param key:
        :return:
        '''

        curr = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not curr.children[index]:
                return False, False
            curr = curr.children[index]

        return curr != None, curr.is_word_end