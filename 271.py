# 271. Encode and Decode Strings
# Array / String / Design

# https://leetcode.com/problems/encode-and-decode-strings/editorial/
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str = ''
        for s in strs:
            encoded_str += s.replace('/', '//') + '/:'
        return encoded_str

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_strs = []
        current_str = ''
        i = 0

        while i < len(s):
            if s[i: i+2] == '/:':
                decoded_strs.append(current_str)
                current_str = ''
                i += 2
            elif s[i:i+2] == '//':
                current_str += '/'
                i += 2
            else:
                current_str += s[i]
                i += 1
        return decoded_strs


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))