


test_input = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """



sum = 0

rows = []
results = []

f = open("06/input.txt", 'r')
lines = f.readlines()
#lines = test_input.split('\n')

line_len = len(lines[0])
num_rows = len(lines)
print("Line len: ", line_len, " Num rows: ", num_rows)

# print lengths of all lines
for i in range(num_rows):
    print("Line ", i, " len: ", len(lines[i]))


additions = []
multiplications = []
column_numbes_index = -1
column_numbers = []
multiply = False
for i in range(line_len):
    print("Processing column ", i)
    column_numbers.append("")
    column_numbes_index += 1
    print("Column numbers: ", column_numbers)
    for j in range(num_rows):
        if lines[j][i] == ' ':
            #column_numbes_index += 1
            continue
        elif lines[j][i] == '\n':
            break
        elif lines[j][i] == '*':
            multiply = True
            print("MULT")
        elif lines[j][i] == '+':
            multiply = False
            print("ADD")
        else:
            print("Adding char ", lines[j][i], " to column_numbers[", column_numbes_index, "]")
            column_numbers[column_numbes_index] += lines[j][i]
            
    print("Column ", i," number: ", column_numbers[column_numbes_index])

    if column_numbers[column_numbes_index].strip() == '':
        # new column
        print("New COL")
        if multiply:
            print("Adding to multiplications: ", column_numbers)
            multiplications.append(column_numbers)
        else:
            print("Adding to additions: ", column_numbers)
            additions.append(column_numbers)
        column_numbers = []
        column_numbes_index = -1
        multiply = False


print("LAST COL")
if multiply:
    print("Adding to multiplications: ", column_numbers)
    multiplications.append(column_numbers)
else:
    print("Adding to additions: ", column_numbers)
    additions.append(column_numbers)


print("Multiplications: ", multiplications)
print("Additions: ", additions)

sums = []
mult_sum = 1
for m in multiplications:
    mult_sum = 1
    for val in m:
        if val.strip() == '':
            continue
        print("Multiplying ", mult_sum, " by ", int(val))
        mult_sum *= int(val)
    print("Multiplication result: ", mult_sum)
    sums.append(mult_sum)

add_sum = 0
for a in additions:
    for val in a:
        if val.strip() == '':
            continue
        sums.append(int(val))

sum = 0
for s in sums:
    sum += s

print("Sum: ", sum)

exit()
