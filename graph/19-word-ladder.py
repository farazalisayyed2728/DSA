from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        f = set(wordList)

        if endWord not in f:
            return 0

        q = deque()
        q.append((beginWord, 1))

        f.discard(beginWord)

        while q:
            s, val = q.popleft()

            if s == endWord:
                return val

            for i in range(len(s)):
                c = s[i]

                for j in range(97, 123):
                    ch = chr(j)

                    if c == ch:
                        continue

                    new_word = s[:i] + ch + s[i+1:]

                    if new_word in f:
                        q.append((new_word, val + 1))
                        f.remove(new_word)

        return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

solution = Solution()
print(solution.ladderLength(beginWord, endWord, wordList))