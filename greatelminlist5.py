l = map(int,raw_input("Enter the list of values").split())

def greatestnumber(l):
    maxnum = l[0]
    for i in l:
        if maxnum < i:
            maxnum = i
    return maxnum

print greatestnumber(l)
