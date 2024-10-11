class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        return (sum([set(x).issubset(set(allowed)) for x in words]))
        