class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # UNION FIND
        par = [i for i in range(len(edges) + 1)]
        rnk = [1] * (len(edges) + 1)
        
        # iteratively return root parent
        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]] # skip a generation for faster access
                p = par[p]
            return p
        def union(n, m):
            pn, pm = find(n), find(m)
            if pn == pm:
                return False
            if rnk[pn] > rnk[pm]:
                par[pm] = pn
                rnk[pm] += rnk[pn]
            else:
                par[pn] = pm
                rnk[pn] += rnk[pm]
            return True

        for n, m in edges:
            if not union(n, m):
                return [n, m]