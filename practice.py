import random


stuff = ["bread", "eggs", "milk"]
print(stuff)

n = len(stuff)
print "n = ", n

first = stuff[0]
second = stuff[1]
third = stuff[2]
print first, second, third

last = stuff[-1]
print last

print random.choice(stuff)

p1 = (2,3)
p2 = p1
print(p2)

L1 = ['a', 'b', 'c']
L2 = L1
L2.append('d')
print L1

print '# setup'
ls = [ "joe", "jane" ]
print ls

print '\n# adding elements'
ls.append("rob")
ls.extend(["bill", "phoebe"])
ls.insert(2, "marcus")
print ls

print '\n# removing elements'
name = ls.pop(2)
print "removed: ", name

print '\n# sorting elements'
ls.sort()
print ls

ls = ["joe", "jane", "marcus", "rob", "bill", "phoebe"]

x = 'marcus'
if x in ls:
    i = ls.index(x)
    print "removing element [", x, "] at index", i
    ls.remove(x)

print ls


x = 0
while (x < 10):
    print x, ", ",
    x+=1
print

#nested loops
rows = 5
cols = 5

for i in range(rows):
    print i, ":\t",
    for j in range(cols):
        print j, "\t",
    print

def numbers(n):
    x = 0
    while (x < n):
        yield x
        x += 1
#access using next
g = numbers(3)
print next(g)
print next(g)
print next(g)

for x in numbers(10):
    print x, '-',
print

#cast to list
print list(numbers(5))

def recurse(n):
    if(n==0):
        return

    print n, ", ",

    recurse(n-1)

recurse(10)
