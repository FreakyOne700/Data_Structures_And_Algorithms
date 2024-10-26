class ZAlgorithm:
    def __init__(self,pattern,text) -> None:
        self.pattern = pattern
        self.S = pattern + text
        self.Z = [0 for _ in range(len(self.S))]

    def construct_z_table(self):
        self.Z[0] = len(self.S)
        left = 0
        right = 0
        
        for k in range(1,len(self.S)):
            if k > right:
                n = 0
                while n+k<len(self.S) and self.S[n] == self.S[n+k]:
                    n = n+1
                self.Z[k] = n
                if n> 0:
                    left = k
                    right = k+n-1
            else:
                p = k - left

                if self.Z[p] < right-k+1:
                    self.Z[k] = self.Z[p]
                else:
                    i = right+1
                    while i < len(self.S) and self.S[i] == self.S[i-k]:
                        i +=1
                    self.Z[k] = i - k
                    left = k
                    right = i - 1



                    

    def search(self):
        self.construct_z_table()

        for i in range(1,len(self.Z)):
            if self.Z[i] >= len(self.pattern):
                print("Found Match at index %s" % (i - len(self.pattern)))

if __name__ == '__main__':
    algorithm = ZAlgorithm("aabza","abzcaabzaabza")
    algorithm.search()