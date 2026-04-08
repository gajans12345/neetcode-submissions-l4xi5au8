class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_characters = sorted(s)
        sorted_string = "".join(sorted_characters)
        sorted_characters1 = sorted(t)
        sorted_string1 = "".join(sorted_characters1)
        if sorted_string == sorted_string1:
            return True
        else:
            return False
        