os.chdir("C://Users/김용진/Documents/Git")
with open("rosalind_gc.txt") as f :
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

result_value=0

for i in list(seq_dict.keys()):
  count_G=seq_dict[i].count("G")
  count_C=seq_dict[i].count("C")
  seq_length=len(seq_dict[i])
  GC_content=(count_G+count_C)/seq_length * 100
  GC_content=round(GC_content, ndigits=6)
  seq_dict[i]=GC_content
  if GC_content > result_value:
    result_id=i[1:]
    result_value=GC_content

print(result_id)
print(result_value)
  