# Ke Shi on July 29th, 2022

class Trienode:
    def __init__(self, num_pass  = 0, num_end = 0, nexts = []):
        self.num_pass = num_pass
        self.num_end = num_end
        self.nexts = nexts

# Algorithms about Trie

def insert(word):
    if word == None:
        return
    word = list(word)
    trie = Trienode(nexts = [None for _ in range(26)])
    root = trie
    trie.num_pass += 1
    for i in range(len(word)):
        index = ord(word[i]) - ord('a')
        if trie.nexts[index] == None:
            trie.nexts[index] = Trienode(nexts = [None for _ in range(26)])
        trie = trie.nexts[index]
        trie.num_pass += 1
    trie.num_end += 1
    return root

def search(word, trie):
    root = trie
    if word == None:
        return 0
    word = list(word)
    for i in range(len(word)):
        index = ord(word[i]) - ord('a')
        if trie.nexts[index] == None:
            return 0
        trie = trie.nexts[index]
    return trie.num_end

def prefix_number(pre, trie):
    if pre == None:
        return 0
    pre = list(pre)
    for i in range(len(pre)):
        index = ord(pre[i]) - ord('a')
        if trie.nexts[index] == None:
            return 0
        trie = trie.nexts[index]
    return trie.num_pass

def delete(word, trie):
    if search(word, trie) != 0:
        word = list(word)
        trie.num_pass -= 1
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if trie.num_pass == 0:
                trie.nexts = None
                return
            trie = trie.nexts[index]
        trie.num_end -= 1
    else:
        return trie


result1 = insert("abcd")
result2 = search("abcd", result1)
result3 = search("ab", result1)
result4 = prefix_number("ab", result1)
result5 = delete("abcd", result1)






