class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "AUGH"
        string = "augh".join(strs)
        return string

    def decode(self, s: str) -> List[str]:
        if s == "AUGH":
            return []
        string = s.split("augh")
        return string
