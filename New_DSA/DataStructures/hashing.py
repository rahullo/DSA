class Hashing:
    hashTable = {}

    def insert(self,key, val):
        self.hashTable[key] = val
    
    def fetch(self, key):
        return self.hashTable[key]
    

hash1 = Hashing()

hash1.insert("Rahul", 23)
hash1.insert("Yash", 24)
hash1.insert("Chandan", 22)

print(hash1.fetch("Chandan"))