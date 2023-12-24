# https://www.youtube.com/watch?v=RcZsTI5h0kg&ab_channel=Codebagel
# using hash maps
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        result = []
        for s in strs:
            # sort by alphabetical order
            # doing this, regardless of the word it will be the same
            # because keys are immutable, we have to make it so by using tuple
            # example for bat 
            # strs = [bat,hello,yes]
            # strs[0] = s
            # bat = [a,b,t] <- is the key
            sorted_s = tuple(sorted(s))
            # [a.b,t] is appended to bat
            anagram_map[sorted_s].append(s)
        
        #print(anagram_map.values())
        
        for value in anagram_map.values():
            result.append(value)

        return result