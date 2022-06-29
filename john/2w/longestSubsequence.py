class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        binary_str = "{0:b}".format(k)
        max_binary_length = len(binary_str)
        if max_binary_length > len(s):
            return len(s)
        if binary_str >= s[-max_binary_length:]:
            return s[:-max_binary_length].count("0") + max_binary_length
        else:
            return s[:-max_binary_length + 1].count("0") + max_binary_length - 1
