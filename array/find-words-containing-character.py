class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        # Return index i for every word in words where character x is present
        return [i for i, word in enumerate(words) if x in word]