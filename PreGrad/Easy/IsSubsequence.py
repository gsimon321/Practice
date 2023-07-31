from queue import Queue

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        qT = Queue(maxsize = len(t))
        newT = ""
        sC = 0
        
        for i in range(len(t)):
            qT.put(t[i])
        for i in range(len(t)):
            if(sC == len(t)):
                break
            tC = qT.get()
            print(tC)
            if(s[sC] == tC):
                newT+=tC
                sC = sC + 1
        if(newT == s):
            return True
        else:
            return False