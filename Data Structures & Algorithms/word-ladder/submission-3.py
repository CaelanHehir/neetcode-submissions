class Solution:
    def one_letter_off(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False
        diffs = 0
        for c1, c2 in zip(a, b):
            if c1 != c2:
                diffs += 1
                if diffs > 1:
                    return False
        return diffs == 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            current, moves = queue.popleft()
            if current == endWord:
                return moves
            for word in word_set:
                if word not in visited and self.one_letter_off(current, word):
                    visited.add(word)
                    queue.append((word, moves + 1))

        return 0
