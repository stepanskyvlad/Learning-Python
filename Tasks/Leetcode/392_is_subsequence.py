# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of
# the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence
# of "abcde" while "aec" is not).
class Solution:
    @staticmethod
    def isSubsequence(s: str, t: str) -> bool:
        new_str = ''
        ind = 0
        if not s:
            return True
        for letter in t:
            if letter == s[ind]:
                new_str += letter
                ind += 1
                if new_str == s:
                    return True
        else:
            return False


if __name__ == "__main__":
    s = Solution
    print(s.isSubsequence("ab", "baab"))
