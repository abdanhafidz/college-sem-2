class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in hash_map:
                hash_map[key].append(s)
            else:
                hash_map[key] = [s]
        return list(hash_map.values())