# Unique Morse Code Words
# String

# runtime: faster than 95.40%
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        seen = set()
        seen = { ''.join(code[ord(c)-ord('a')] for c in word) for word in words}
        return len(seen)