'''
Transcribing DNA into RNA
'''

DNA=list(input("write DNA sequence"))

RNA=""
for i in DNA:
    if i == 'A':
        RNA=RNA+"U"
    elif i == 'T':
        RNA=RNA+"A"
    elif i == 'G':
        RNA=RNA+"C"
    elif i == 'C':
        RNA=RNA+"G"
    else :
        print("Not DNA sequence included")
        break

print(RNA)