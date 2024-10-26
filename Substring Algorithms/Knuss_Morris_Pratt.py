def construct_pi(pattern):
    pi_table = [0]*len(pattern)

    prefix_counter = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[prefix_counter]:
            prefix_counter = prefix_counter+1
            pi_table[i] = prefix_counter
            i +=1
        else:
            if prefix_counter != 0:
                prefix_counter = prefix_counter-1
            else:
                pi_table[i] = 0
                i+=1
    return pi_table

def search(text,pattern):
    pi_table = construct_pi(pattern)

    i = 0
    j = 0

    while i < len(text) and j < len(pattern):
        if text[i] == pattern[j]:
            i+=1
            j+=1
        if j == len(pattern):
            print("Found at Index %s" % (i-j))
            j = pi_table[j-1]
        elif i<len(text) and text[i] != pattern[j]:
            if j!=0:
                j = pi_table[j-1]
            else:
                i +=1



if __name__ == "__main__":
    search("aacaabaab","aab")