# Encode and Decode TinyURL
# String / Hash Table

# https://blog.csdn.net/fuxuemingzhu/article/details/79264976

# String
# runtime: faster than 98.03%
class Codec:
    def __init__(self):
        self.urls = []
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.urls.append(longUrl)
        return "http://tinyurl.com/" + str(len(self.urls) - 1)
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urls[int(shortUrl.split('/')[-1])]


# Hash Table
# runtime: faster than 50.04% 
class Codec:
    def __init__(self):
        self.count = 0
        self.d = {}
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.count += 1
        self.d[self.count] = longUrl
        return str(self.count)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.d[int(shortUrl)]