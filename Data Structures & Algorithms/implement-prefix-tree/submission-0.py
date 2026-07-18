class PrefixTree:

    def __init__(self):
        self.start={}

    def insert(self, word: str) -> None:
        node=self.start
        for i, char in enumerate(word):
            if char in node:
                node=node[char]
            else:  
                node[char]={}
                node=node[char]
            if i == (len(word)-1):
                node["end"]=True

    def search(self, word: str) -> bool:
        node=self.start
        for char in word:
            if char in node:
                node=node[char]
            else:
                return False
        return True if "end" in node else False
        

    def startsWith(self, prefix: str) -> bool:
        res=""
        node=self.start
        for char in prefix:
            if char in node:
                res=res+char
                node=node[char]
            else:
                return False
        return True





