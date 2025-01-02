class Solution():
    def vowelStrings(words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        def vowelStrings(self, words, queries):
        prefix = []
        res = []
        count = 0

        def isVowel(c):
            return c in 'aeiou'

        for word in words:
            if isVowel(word[0]) and isVowel(word[-1]):
                count += 1
            prefix.append(count)

        for query in queries:
            l, r = query
            if l == 0:
                res.append(prefix[r])
            else:
                res.append(prefix[r] - prefix[l - 1])

        return res
            







words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]

a = Solution()
print(a.vowelStrings(words,queries))


# Example 1:

# Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
# Output: [2,3,0]
# Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
# The answer to the query [0,2] is 2 (strings "aba" and "ece").
# to query [1,4] is 3 (strings "ece", "aa", "e").
# to query [1,1] is 0.
# We return [2,3,0].
