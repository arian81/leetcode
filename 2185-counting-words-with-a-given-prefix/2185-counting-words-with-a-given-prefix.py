class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(map(lambda x: x.startswith(pref), words))
        