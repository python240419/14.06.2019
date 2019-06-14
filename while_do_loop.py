# foreach
# for number in numbers: ....

# for
# for n in range(....)

# loop when the exit-condition is unknown.... while
# do-while / while

# do-while: will run the 1st iteration before checking the condition
while True:
    y = int(input('Enter number: '))
    print(y)
    if y <= 0:
        break


# while: will first check the condition before making the 1st iteration
x = 1
while x > 0: # exit when the condition if false!
    x = int(input('Enter number: '))
    print(x)

# write a while loop which inputs a number from the user
# each time print the numbers between 1- number inputed
# the loop will terminate when the input number was 0 or below
# if the user enter 1 then ignore, and skip to next iteration
x = 1
while x > 0:
    x = int(input('Enter number: '))

    if x == 1:
        continue

    print(f'the number is: {x}')
    for n in range(1, x + 1):
        print(n)

# calculate average of class, until average was above 90
# to exit enter negative number - break
# when grade was zero continue - student without grade, ignore
avg = 0
sum = 0
counter = 0
while avg <= 90: # exit condition is always opposite
    grade = int(input('Enter grade: '))
    if grade < 0:
        break
    if grade == 0:
        continue
    sum = sum + grade
    counter = counter + 1
    avg = sum / counter

print('outside loop............')
