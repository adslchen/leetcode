class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ex_times = [0]*n
        function_stack = []
        
        prev_time = 0
        last_state = None
        for log in logs:
            log_id = int(log.split(":")[0])
            state = log.split(":")[1]
            time = int(log.split(":")[2])
            if function_stack:
                period = time - prev_time
                if state == 'start' and last_state == 'end':
                    period -= 1
                elif state == 'end' and last_state == 'start':
                    period += 1
                ex_times[function_stack[-1]] += period
                
            if state == 'start':
                function_stack.append(log_id)
            else:
                function_stack.pop()
                
            last_state = state
            prev_time = time
            
        return ex_times
