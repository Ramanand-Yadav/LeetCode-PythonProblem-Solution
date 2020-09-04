class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or len(A) < 2:
            return False

        diffs = [[a, b] for a, b in zip(A, B) if a != b]
        if len(diffs) == 2:
            return diffs[0][::-1] == diffs[1]

        return len(diffs) == 0 and len(set(A)) < len(A)
