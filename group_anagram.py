class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    results = []
    hashmap = {}
    paired_anagrams = []
    for i in range(len(strs)):
      word = sorted(strs[i])
      word = ''.join(word)
      if hashmap:
        if word in hashmap:
          value = hashmap[word]
          value.append(strs[i])
        else:
          paired_anagrams = []
          paired_anagrams.append(strs[i])
          hashmap[word] = paired_anagrams
        else:
          paired_anagrams.append(strs[i])
          hashmap[word] = paired_anagrams

          for key in hashmap:
            results.append(hashmap[key])
        # returns results
        return results