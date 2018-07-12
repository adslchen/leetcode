from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        def buildDict(wordList):
            dictionary = {}
            for word in wordList:
                for i in range(len(word)):
                    key = word[:i] + "_" + word[i+1:]
                    dictionary[key] = dictionary.get(key, []) + [word]
                    
            return dictionary
        def BFS(dictionary, begin, end):
            visit = set()
            queue = deque([(begin, 1)])
            while queue:
                word, step = queue.popleft()
                if word == end:
                    return step
                visit.add(word)
                for i in range(len(word)):
                    key = word[:i]+ "_" + word[i+1:]
                    neighbors = dictionary.get(key, [])
                    if neighbors:
                        for nei in neighbors:
                            if nei not in visit:
                                queue.append((nei,step+1))
            return 0
        
        d = buildDict(set(wordList ))
        step = BFS(d, beginWord, endWord)
        return step
                        
