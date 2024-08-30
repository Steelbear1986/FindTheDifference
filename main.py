class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = Counter(s)
        t = Counter(t)
        for v, k in t.items():
            if t[v] != s[v] or v not in t:
                return v
