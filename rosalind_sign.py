import itertools

#문제 불러오기
with open("rosalind_sign.txt","r") as f:
    sample=int(f.read())

#negative sign number 만들기
num=[]
for i in range(1,sample+1) :
    num.append(i)
    num.append(-i)
num.sort()

#모든 combination 구하기
def get_all_comb(x):
    result=[]
    for i in itertools.combinations(x,sample):
        result.append(list(i))
    return result
all_comb=get_all_comb(num)

#같은 절대 값 숫자가 들어간 리스트 제거하기
def remove_dup_comb(x):
    result=[]
    for comb in all_comb:
        #remove dup
        tmp=[]
        for i in comb:
            tmp.append(abs(i))
        if len(tmp) == len(set(tmp)):
            result.append(comb)
    return result
comb_rmDup=remove_dup_comb(all_comb)

#모든 permutated(자리가 바뀐) 리스트 구하기
def get_permutated_comb(x):
    result=[]
    for comb in x:
        for sub in itertools.permutations(comb,sample):
            int_to_str=[str(i) for i in sub]
            comb_str=" ".join(int_to_str)
            result.append(comb_str)
    return result
result=get_permutated_comb(comb_rmDup)

#결과를 text file로 저장하기
with open("rosalind_sign.output.txt","w") as f:
    f.write(str(len(result))+"\n")
    f.write("\n".join(result))