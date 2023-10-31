class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for idx, (var1, var2) in enumerate(equations):
            graph[var1].append((var2, values[idx]))
            graph[var1].append((var1, 1))
            graph[var2].append((var1, 1 / values[idx]))
            graph[var2].append((var2, 1))
            
        dp = {}
        def evaluate(q1, q2):
            if (q1, q2) in dp: return dp[(q1, q2)]
            
            for var1, value1 in graph[q1]:
                for var2, value2 in graph[q2]:
                    if var1 == var2:
                        dp[(q1, q2)] = value1 / value2
                        return dp[(q1, q2)]
            
            caller_set.add(q1)      
            for var1, value1 in graph[q1]:
                if var1 in caller_set: continue
                result = evaluate(var1, q2)
                if result != -1:
                    dp[(q1, q2)] = value1 * result
                    return dp[(q1, q2)]
            
            dp[(q1, q2)] = -1
            return dp[(q1, q2)]
    
        ans = []
        for var1, var2 in queries:
            caller_set = set()
            ans.append(evaluate(var1, var2))
        return ans
        
        
        
"""

{'x1': [('x2', 3.0), ('x1', 1)],

'x2': [('x1', 0.3333333333333333), ('x2', 1), ('x3', 4.0), ('x2', 1)], 

'x3': [('x2', 0.25), ('x3', 1), ('x4', 5.0), ('x3', 1)], 

'x4': [('x3', 0.2), ('x4', 1), ('x5', 6.0), ('x4', 1)], 

'x5': [('x4', 0.16666666666666666), ('x5', 1)]}

"""