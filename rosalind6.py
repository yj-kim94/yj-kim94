with open("rosalind_lcsm.txt","r") as f :
    lines=f.readlines()

str_dict={}
for i in range(len(lines)):
    if lines[i][0]==">":
        str_dict[lines[i].strip()]=""
        n=1
        while lines[i+n][0]!=">":
            print(lines[i+n],end="")
            str_dict[lines[i].strip()]+=lines[i+n].strip()
            n+=1
            if len(lines)==(i+n):
                break
    else : continue