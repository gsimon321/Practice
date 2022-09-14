# creating a TrieNode
class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []
    
def WordSquare(words: list[str]):
    # declaring a starting node
    root = TrieNode()
    # helper functions
    # helper to populate the trie structure
    def insertion(word):
        cur = root
        # this is for every single character in the word
        for c in word:
            # if the character is not in the children of the current node we add it
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # switch the current node to the new child node of the old current node
            cur = cur.children[c]
            cur.words.append(word)

    def getWords(prefix):
        cur = root

        for c in prefix:
            if c not in cur.children:
                return []
            cur = cur.children[c]
    
    def trace(curWords, index):
        if index == lengthOfWords:
            answer.append(curWords[:])
            return
        # this is the prefix that is computed
        prefix =  ''.join(word[index] for word in curWords)

        words = getWords(prefix)

        for word in words:
            curWords.append(word)
            trace[index+1,curWords]
            curWords.pop()
        


    #This is going to be for building the trie itself
    for word in words:
        insertion(word)
    
    # this is where the back tracking will start off
    answer = []
    lengthOfWords = len(words[0])

    for word in words:
        trace([word], 1)        
    

newArray = ["ab","ba"]
print(WordSquare(newArray))