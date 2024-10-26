class RabinKarp:
    def __init__(self,pattern,text):
        self.pattern = pattern
        self.text = text

        self.d = 26
        self.q = 31
    def search(self):
        m = len(self.pattern)
        n = len(self.text)
        hash_text = 0
        hash_pattern = 0 
        h = 1

        for _ in range(m-1):
            h = (h*self.d) % self.q
        for i in range(m):
            hash_pattern = (self.d * hash_pattern + ord(self.pattern[i])) % self.q
            hash_text = (self.d * hash_text + ord(self.text[i])) % self.q
        for i in range(n-m+1):
            if hash_text == hash_pattern:
                j = 0
                while j<m:
                    if self.text[i+j] != self.pattern[j]:
                        break
                    j+=1
                if j == m:
                    print("Found at Index %s" % i)
            if i < n-m:
                hash_text = ((hash_text - ord(self.text[i]) * h) * self.d + ord(self.text[i+m])) % self.q
                if hash_text < 0:
                    hash_text = hash_text + self.q

if __name__ == '__main__':
    algorithm = RabinKarp("text","This is a text")
    algorithm.search()
