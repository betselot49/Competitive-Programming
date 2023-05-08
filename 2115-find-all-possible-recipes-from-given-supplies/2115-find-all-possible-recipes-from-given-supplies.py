class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        queue = deque([])
        for ind, recipe in enumerate(recipes):
            all_found = True
            for ingredient in ingredients[ind]:
                if ingredient not in supplies:
                    all_found = False
            if all_found:
                queue.append(ind)
                
        done = set()     
        order = []
        while queue:
            curr = queue.popleft()
            if recipes[curr] in done: continue
            done.add(recipes[curr])
            supplies.add(recipes[curr])
            order.append(recipes[curr])
            for ind, recipe in enumerate(recipes):
                if recipe in done: continue
                all_found = True
                for supply in ingredients[ind]:
                    if supply not in supplies:
                        all_found = False
                if all_found:
                    queue.append(ind)
        
        return order