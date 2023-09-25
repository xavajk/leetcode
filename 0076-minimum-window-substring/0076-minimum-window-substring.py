class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '': return t
        
        s_map = defaultdict(int)
        t_map = defaultdict(int)
        for c in t: t_map[c] += 1

        have, need = 0, len(t_map)
        l, res = 0, ('', float('inf'))
        for r in range(len(s)):
            s_map[s[r]] += 1
            if s[r] in t and s_map[s[r]] == t_map[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) < res[1]:
                    res = (s[l:r + 1], r - l + 1)
                s_map[s[l]] -= 1
                if s[l] in t and s_map[s[l]] < t_map[s[l]]:
                    have -= 1
                l += 1
        return res[0]