'''
Finding a Motif in DNA
'''

with open("rosalind_subs.txt","r") as f :
    DNA=f.readlines()

result=""
end=len(DNA[1])

for i in range(len(DNA[0])):
    if DNA[0][i:i+end]==DNA[1]:
        print(DNA[0][i:i+end])
        result+=(str(i+1)+" ")
    else:
        continue
print(result)