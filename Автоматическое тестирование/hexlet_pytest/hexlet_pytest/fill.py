def fill(coll, value, begin=0, end=0):
    end = len(coll) if end > len(coll) or end == 0 else end
    while begin < end:
        coll[begin] = value
        begin += 1

coll =  [1, 2, 3, 4]
 
#fill(coll, '*', 1, 3)
print(coll)  # => [1, '*', '*', 4]
 
fill(coll, '*')
print(coll)  # => ['*', '*', '*', '*']
 
#fill(coll, '*', 4)
print(coll)  # => [1, 2, 3, 4]
 
#fill(coll, '*', 0, 10)
print(coll)  # => ['*', '*', '*', '*']