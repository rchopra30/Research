import tensorflow as tf

thisset = set()

t = ['', '', '', 'd']

for x in t:
    if len(thisset) < 3:
        thisset.add(x)
        if x in thisset:
            print(x)
print(thisset)

s = 'wow this is cool'
a = s.split('wow this is')
print(a)
