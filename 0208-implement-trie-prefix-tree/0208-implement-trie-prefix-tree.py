class Trie:

    def __init__(self, val=""):
        self.children = {}
        self.is_word = False

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.is_word = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.is_word

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)