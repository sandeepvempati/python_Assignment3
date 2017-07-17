l = map(int,raw_input("Enter a list of values").split())
l1 =[]

while l:
    min = l[0]
    for i in l:
        if i<min:
            min = i
    l1.append(min)
    l.remove(min)


print l1
print l

