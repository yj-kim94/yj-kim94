'''
Counting Point Mutations
'''

with open("rosalind_hamm.txt","r") as f:
  lines=f.readlines()

DNA_1=lines[0]
DNA_2=lines[1]

result=0
if len(DNA_1)==len(DNA_2):
    for i in range(len(DNA_1)):
        if DNA_1[i]!=DNA_2[i]:
            result=result+1
        else:
            continue
    print(result)
else:
    print("Two sequences' lengths are not matched")