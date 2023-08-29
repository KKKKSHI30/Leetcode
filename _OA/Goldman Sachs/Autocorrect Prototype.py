# 题目:  https://www.1point3acres.com/bbs/thread-1010797-1-1.html
def getSearchResults(words, queries):
    # Create a dictionary to store anagrams
    anagram_dict = {}

    # Group words by their sorted characters
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]

    # Find anagrams for each query
    results = []
    for query in queries:
        sorted_query = ''.join(sorted(query))
        if sorted_query in anagram_dict:
            results.append(sorted(anagram_dict[sorted_query]))
    return results

words = ["duel", "speed", "dule", "cars"]
queries = ["spede", "deul"]
getSearchResults(words, queries)
getSearchResults(["allot","cat", "peach", "dusty","act", "cheap"], ['tac', 'study', 'peach'])