'''
Finding a Shared Motif
'''

os.chdir("C://Users/김용진/Documents/Git")
with open("rosalind_lcsm.txt","r") as f :
    lines=f.readlines()

seq_dict={}

for i in range(len(lines)):
    if lines[i][0]==">":
        seq_dict[lines[i].strip()]=""
        n=1      
        while lines[i+n][0]!=">":
            seq_dict[lines[i].strip()]+=lines[i+n].strip()
            n+=1
            if len(lines)==(i+n):
                break
    else : continue

def lcs(S,T):
    m = len(S)
    n = len(T)
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    lcs_set = set()
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_set = set()
                    longest = c
                    lcs_set.add(S[i-c+1:i+1])
                elif c == longest:
                    lcs_set.add(S[i-c+1:i+1])

    return lcs_set

result=list(lcs(seq_dict[sequence[0]],seq_dict[sequence[1]]))[0]
for i in range(len(sequence)) : 
  lcs(result,seq_dict[sequence[i]])
print(result)    