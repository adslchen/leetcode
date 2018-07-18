class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost): return -1
        minGas = 2**31-1
        minIndex = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank <= minGas:
                minGas = tank
                minIndex = i
                
        return (minIndex+1)%len(gas)
