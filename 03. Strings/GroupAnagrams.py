# Time: O(W * Nlog(N) + N * Wlog(W)) | Space: O(W*N)
def groupAnagrams(words):
    if len(words) == 0:
        return []
    
    sortedWords = ["".join(sorted(w)) for w in words]
    indices = [i for i in range(len(words))]
    indices.sort(key=lambda x: sortedWords[x])
    
    result = []
    currentAnagramGroup = []
    currentAnagram = sortedWords[indices[0]]
    for index in indices:
        word = words[index]
        sortedWord = sortedWords[index]
        
        if sortedWord == currentAnagram:
            currentAnagramGroup.append(word)
            continue
        
        result.append(currentAnagramGroup)
        currentAnagramGroup = [word]
        currentAnagram = sortedWord
    result.append(currentAnagramGroup)
    return result

# Time: O(W * Nlog(N)) | Space: O(W*N)
def groupAnagrams1(words):
    anagrams = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
    return list(anagrams.values)
