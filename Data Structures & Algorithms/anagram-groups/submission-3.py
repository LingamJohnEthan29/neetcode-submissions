from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for i in strs:
            count_arr = [0]*26
            for j in i:
                count_arr[ord(j)-ord('a')] += 1
            hash_map[tuple(count_arr)].append(i)
        return list(hash_map.values())