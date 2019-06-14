# boolean
a = 12
isABiggerThan10 = a > 10
if isABiggerThan10: #isABiggerThan10 == True:
    print('a bigger than 10')

# 3
numbers = [1, 5, 7, 8, 100]

for number in numbers[ : len(numbers) // 2]:
    print(number)

# 4
words = ['coding of world', 'pen', 'python', 'hello']
for word in words:
    print(word.upper())

# 5
words = ['coding of world', 'pen', 'python', 'hello']
for word in words:
    if len(word) < 4:
        break
    else:
        print(word.upper())

# 6
name = "Donald Trump"
print(name[-5:])
print(name[:len(name) // 3])
print(name.upper().count('a'))
print(name.upper().count('L')) # extra
doesBAppear = name.upper().count('B') > 0
print(doesBAppear)
splitNames = name.split() # ['Donald', 'Trump']
fname_ = splitNames[0]
lname_ = splitNames[1]
fname = name.split()[0]
lname = name.split()[1]
splitNames.reverse()
print(splitNames)
splitNames[0] = splitNames[0].upper()
print(splitNames)
fname = splitNames[0]
nameWithoutMiddleChar = fname[:len(fname)//2] + fname[len(fname)//2 + 1:]
#del splitNames[1][len(splitNames[1]) // 2]
listOfChar = list(splitNames[1])
del listOfChar[len(listOfChar) // 2]
splitNames[1] = ''.join(listOfChar)
print(splitNames)
splitNames.insert(1, ' ')
print(splitNames)
newName = ''.join(splitNames)
print(newName)

names = ['ab', 'cd', 'ef']
result = ""
for name in names:
    result = result + name + ' '
print(result)

# 7 - 8
sen = "Hello World!"
print(sen.upper().find("O"))
print(sen[:sen.upper().find("O")])
print(sen[sen.upper().rfind("O"):])
print(sen.replace("o", ""))

# 9
nlist = [8, 1000, -3, 2, 5]
print(sum(nlist))
print(max(nlist))
print(min(nlist))
print(sum(nlist) / len(nlist))
del nlist[len(nlist) // 2]
print(nlist)
nlist = [8, 1000, -3, 2, 5]
nlist.sort()
print(nlist)
print(nlist * 5)
del nlist[0]
print(nlist)
nlist = [8, 1000, -3, 2, 5]

average = sum(nlist) / len(nlist)
print(f'Average is {average}')
underAvg = []
for number in nlist:
    if number < average:
        underAvg.append(number)
print(underAvg)

# 10 find max
ylist = [100, 108, 7, 5, 1, 204, -100, 9]
ymax = ylist[0]
for number in ylist[1:]:
    if number > ymax:
        ymax = number
print(f'max is {ymax}')
print(f'was I right? {ymax == max(ylist)}')

# 11
listofLists = [[4, 8, 200], [4, 3000, -1, 2, 9, 105], [5, 87, 12, -7]]
ymin = listofLists[0][0]
for pList in listofLists:
    for oneNumber in pList:
        if oneNumber < ymin:
            ymin = oneNumber
print(f'min is {ymin}')


