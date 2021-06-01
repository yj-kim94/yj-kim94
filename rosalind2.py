DNA_1="GAGCCTACTAACGGGAT"
DNA_2="CATCGTAATGACGGCCT"

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