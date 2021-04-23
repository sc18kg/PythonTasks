mylist = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
newlist =[]

for item in mylist:
  if item % 2 == 0:
    newlist.append(item)
    
print(newlist)
