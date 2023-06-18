import random
# RandomPool which insert, delete and get a random value in O(1) time
class random_pool():
    def __init__(self):
        self.keyindex = {}
        self.indexkey = {}
        self.size = 0

    def insert(self, key):
        if key not in self.keyindex:
            self.keyindex[key] = self.size
            self.indexkey[self.size] = key
            self.size += 1

    def delete(self, key):
        if key in self.keyindex:
            deleteindex = self.keyindex[key]
            self.size -= 1
            lastkey = self.indexkey[self.size]
            self.keyindex[lastkey] = deleteindex
            self.indexkey[deleteindex] = lastkey
            self.keyindex.pop(key)
            self.indexkey.pop(self.size)
        else:
            print("cannot remove")

    def random(self):
        rand = random.randint(0, self.size)
        return self.indexkey.get(rand)

result = random_pool()
result.insert("a")
result.insert("b")
result.insert("c")
result.insert("d")
result.delete("a")
result.delete("e")
result.random()


