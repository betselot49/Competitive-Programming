class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = defaultdict(list)
        self.graph[kingName] = []
        self.deaths = set()
        self.kingName = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deaths.add(name)

    def getInheritanceOrder(self) -> List[str]:
        successor = []
        stack = [self.kingName]
        while stack:
            parent = stack.pop()
            if parent not in self.deaths:
                successor.append(parent)
            for children in self.graph[parent][::-1]:
                stack.append(children)
        return successor
                

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()