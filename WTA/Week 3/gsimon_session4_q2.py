def canFinish(self, numCourses, prerequisites):
        def cycle(v, G, R, B):
            if v in R: return True
            R.add(v)
            if v in G:
                for _v in G[v]:
                    if _v not in B and cycle(_v, G, R, B): return True
            R.remove(v); B.add(v)
            return False
        
        G, R, B = collections.defaultdict(list), set(), set()
        for p in prerequisites:
            G[p[0]].append(p[1])
        for v in G:
            if v not in B and cycle(v, G, R, B): return False
        return True