class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = [set(['q','w','e','r','t','y','u','i','o','p']),
                set(['a','s','d','f','g','h','j','k','l']),
                set(['z','x','c','v','b','n','m'])]
        solutions = []
        for word in words:
            new = word.lower()
            for row in rows:
                check = True
                for char in new:
                    if char not in row:
                        check = False
                if check:
                    solutions.append(word)
        return solutions
