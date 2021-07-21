'''
Complementing a Strand of DNA
'''
DNA=input()

DNA=list(DNA)

result=""

for i in DNA :
  if i=="A":
    result=result+"T"
  elif i=="T":
    result=result+"A"
  elif i == "G" :
    result=result+"C"
  elif i == "C" :
    result=result+"G"

print(result[::-1])