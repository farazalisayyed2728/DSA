class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        need = {}
        have = {}

        for i in range(len(ransomNote)):
            need[ransomNote[i]] = need.get(ransomNote[i], 0) + 1

        for j in range(len(magazine)):
            have[magazine[j]] = have.get(magazine[j], 0) + 1

        for i in range(len(ransomNote)):

            
            if need[ransomNote[i]] > have.get(ransomNote[i], 0):

                return False

        return True