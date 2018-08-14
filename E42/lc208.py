class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tries = [None] * 26

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        pointer = self.tries
        for i in range(len(word)):
            ascii = ord(word[i]) - ord('a')
            if pointer[ascii] == None:
                pointer[ascii] = [None] * 26
            pointer = pointer[ascii]
        pointer.append(word)
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        pointer = self.tries
        for i in range(len(word)):
            ascii = ord(word[i]) - ord('a')
            if pointer[ascii] == None:
                return False
            pointer = pointer[ascii]
        if word in pointer[26:]:
            return True
        else:
            return False
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        pointer = self.tries
        for i in range(len(prefix)):
            ascii = ord(prefix[i]) - ord('a')
            if pointer[ascii] == None:
                return False
            pointer = pointer[ascii]
        return True
