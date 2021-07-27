from scipy.special import comb
import os
os.chdir("C://Users/김용진/Documents/Git")

with open("rosalind_iprb.txt","r") as f:
  line=f.read()

hom, het, rec = map(int, line.split())

#전체 발생 가능한 자손의 개수 구하기

#전체 중 2개씩 뽑아 mate를 이룰 경우의 수(조합)
total_comb=comb(hom+het+rec,2)

#각 mate로부터 4개 조합의 자손이 나온다.
total_children=4*total_comb

#열성동형접합을 이룰 경우의 수 
#dom X dom은 열성이 나올 수 없음
#het X het는 1개의 자손이 열성동형
#het X rec는 2개의 자손이 열성동형
#rec X rec는 4개의 자손이 열성동형
total_rec=4*comb(rec,2)+2*het*rec+1*comb(het,2)

#1-열성동형접합 자손이 나올 확률 = 하나 이상의 우성형질을 가진 자손이 나올 확률
prob_dom=1-(total_rec/total_children)
print(prob_dom)