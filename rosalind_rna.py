'''
Transcribing DNA into RNA
'''

DNA=list(input("write DNA sequence"))
print(len(DNA))
RNA=""
for i in DNA:
    if i == 'T':
        RNA=RNA+"U"
    else :
        RNA=RNA+i

print(len(RNA))
print(RNA)