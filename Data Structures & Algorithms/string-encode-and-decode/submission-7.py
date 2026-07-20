class Solution:

    def encode(self, strs: List[str]) -> str:
        strs.append('CACA')
        string = "augh".join(strs)
        return string

    def decode(self, s: str) -> List[str]:
        strings = s.split("augh")
        strings.pop()
        return strings
