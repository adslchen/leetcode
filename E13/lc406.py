class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        peopledict = {}
        
        for index, p in enumerate(people):
            if p[0] in peopledict:
                peopledict[p[0]].append((p[1], index))
            else:
                peopledict[p[0]] = [(p[1], index)]
        
        height = peopledict.keys()
        height.sort()
        print(height)
        result = []
        for h in height[::-1]:
            peopledict[h].sort()
            for p in peopledict[h]:
                result.insert(p[0], people[p[1]])
        return result
