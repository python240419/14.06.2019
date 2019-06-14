# Range
l = [1, 2, 3, 4, 5, 6, -1, 10, -3]

for number in l:
    print(number)

for n in range(5): # 0-4
    print(n)

for n in range(len(l)): # 0-8
    if (l[n] < 0):
        print(f'List[{n}] = {l[n]} is negative')
    else:
        print(f'List[{n}] = {l[n]}')

# find first number 100-200 which divide by 7 without reminder
for n in range(100, 200):
    if n % 7 == 0:
        print(n)
        break

for n in range(0, 200, 15): # third number is jump
    print(n)

# create a list of words
# print the words using the range command
# *print the list backwards using the range command

burgers = ['beef', 'chicken', 'veggie', 'Big america', 'Heart burger'] # len = 5
for n in range(len(burgers)): # 0-4
    print(f'#{n} : {burgers[n]}')

print('backwards:')
for n in range(len(burgers) - 1, -1, -1):    # burgers[5] ==> Error!
    print(f'#{n} : {burgers[n]}')

print('backwards:') # tricky way**
for n in range(-1, -1 * len(burgers) - 1, -1):    # burgers[5] ==> Error!
    print(f'#{n} : {burgers[n]}')

for n in reversed(range(len(burgers))): # tricky way***
    print(f'#{n} : {burgers[n]}')

# create list using range
    
l1 = [2, 4, 5, 6]

l2 = list(range(5))
print(l2)

l3 = list(range(5, 100, 2))
print(l3)

l4 = list(reversed(l3))
print(l4)

x = 5
l5 = list(range(5, 100, x))
print(l5)
