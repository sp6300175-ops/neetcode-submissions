class TrieNode:

    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        nodes = [self.root]
        for ch in word:
            next_nodes = []
            for node in nodes:
                if ch =='.':
                    next_nodes.extend(node.children.values())
                elif ch in node.children:
                    next_nodes.append(node.children[ch])
            nodes = next_nodes
        return any(node.isEnd for node in nodes)
        
