class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self, key):
        return key % self.size

    def rehash(self, oldhash):
        return (oldhash + 1) % self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key)
        # key不存在，未冲突
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            # key存在，替换val
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                # 散列冲突，再散列，直到找到空槽或者key
                nextslot = self.rehash(hashvalue)
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    def get(self, key):
        # 标记散列值为查找起点
        startslot = self.hashfunction(key)
        data = None
        stop = False
        found = False
        position = startslot
        # 找key，直到空槽或者回到起点
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                # 未找到key，再散列继续找
                position = self.rehash(position)
                if position == startslot:
                    # 回到起点，停止
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


if __name__ == '__main__':
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print(H.slots)
    print(H.data)
    print(H[20])
    print(H[17])
    H[20] = 'duck'
    print(H[20])
    print(H[99])
