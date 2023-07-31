class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # mapping from S -> T and then from T -> S
        mapST, mapTS = {}, {}
        #  for loop to traverse over just s but this is all that is needed because we know
        #  that both len(s) == len(t)
        for i in range(len(s)):
            # now we get the mapping pair
            c1,c2 = s[i], t[i]
            # checking if those mapping pairs already exist for other characters
            if ((c1 in mapST and mapST[c1] != c2) or 
                (c2 in mapTS and mapTS[c2] != c1)):
                # then will return false
                return False
            # otherwise it adds them to the maps and then continues
            mapST[c1] = c2
            mapTS[c2] = c1
        # if there is no error than it just returns true
        return True