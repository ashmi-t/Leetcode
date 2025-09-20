class RandomizedSet:

    def __init__(self):
        self.vals = {}  
        self.idxs = []

    def insert(self, val: int) -> bool:
        if val in self.vals : return False 
        self.vals[val] = len(self.idxs)
        self.idxs.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.vals: 
            lst = self.idxs[-1]     
            pos = self.vals[val]
            
            self.vals[lst] = pos   
            self.idxs[pos] = lst             
            
            self.vals.pop(val)                
            self.idxs.pop()                   
            
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.idxs)      