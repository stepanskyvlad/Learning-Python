# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_count = dict()
        c = "a"
        for i in range(len(s)):
            if s[i] in char_count:
                c = char_count[s[i]]
                if c != t[i]:
                    return False
            elif t[i] not in char_count.values():
                char_count[s[i]] = t[i]
            else:
                return False
        return True
