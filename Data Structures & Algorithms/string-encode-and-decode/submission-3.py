class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "AUGH"
        string = "\n".join(s for s in strs)
        return string

    def decode(self, s: str) -> List[str]:
        if s == "AUGH":
            return []
        string = s.split("\n")
        return string
