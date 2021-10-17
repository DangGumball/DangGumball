bruh = (20)
output1 = list(range(bruh))
print(output1)

number1 = int(input('enter a number here: '))
output2 = list(range(number1))
print(output2)

for i in range(1, 20+1):
    if(i  % 2 == 0):
        print('0', end= '  ')
    else:
        print('1', end= '  ')

total_number = int(input('enter the total numbers of 1s and 0s: '))
for j in range(1, total_number+1):
    if(j  % 2 == 0):
        print('0', end= '  ')
    else:
        print('1', end= '  ')

for row in range(0, 10):
    for col in range(0, 10):
        num = row * col
        if num < 10:
            empty = "  "
        else:
            if num < 100: 
                empty  = " " 
        if col == 0:
            if row == 0:
                print("    ", end = '')
            else:
                print("  ", end='')
        elif row == 0:
            print("  ", end='')
        else:
            print(empty, num, end = '')
    print()

number2 = int(input('enter a number: '))
for row in range(0, number2+1):
    for col in range(0, number2+1):
        num = row * col
        if num < number2 + 1:
            empty = "  "
        else:
            if num < (number2+1)* (number2+1) : 
                empty  = " " 
        if col == 0:
            if row == 0:
                print("    ", end = '')
            else:
                print("  ", end='')
        elif row == 0:
            print("  ", end='')
        else:
            print(empty, num, end = '')
    print()

table = [[(i+j)%2 for j in range(11)] for i in range(11)]
for row in table:
    for cell in row:
        print (cell, end=' ')
    print()

row_column = int(input('enter a number: '))
table = [[(i+j)%2 for j in range(row_column + 1)] for i in range(row_column + 1)]
for row in table:
    for cell in row:
        print (cell, end=' ')
    print()