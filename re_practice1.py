import re
test="abcdabcd"

print(test)

#match 
print(re.match("a",test)) #matched
print(re.match("ab",test)) #matched
print(re.match("b",test)) #not matched
print(re.match("bcd",test)) #not matched

print(test)

#search
print(re.search("a",test)) #matched
print(re.search("abc",test)) #matched
print(re.search("b",test)) #matched
print(re.search("cb",test)) #not matched

print(test)

#findall
print(re.findall("a",test))
print(re.findall("ab",test))
print(re.findall("ac",test))

print(test)

#fullmatch
print(re.fullmatch("a",test))
print(re.fullmatch("abcd",test))
print(re.fullmatch("abcdabcd",test))

print(test)

#how to use matchObj
print(re.search("bcd",test).group()) #matched string
print(re.search("bcd",test).start()) #start position
print(re.search("bcd",test).end()) #end position
print(re.search("bcd",test).span()) #tuple

print(test)

#finditer
print(re.finditer("ab",test))

for i in re.finditer("ab",test):
  print(i)

for i in re.finditer("ab",test):
  print(i.group())

for i in re.finditer("ab",test):
  print(i.start())