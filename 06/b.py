


test_input = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

def multiply_nums(nums):
    result = 1
    for n in nums:
        result *= int(n)
    return result

def add_nums(nums):
    result = 0
    for n in nums:
        result += int(n)
    return result

def process_column(column_numbers, multiply):
    if multiply:
        return multiply_nums(column_numbers)
    else:
        return add_nums(column_numbers)

sum = 0

rows = []
results = []

f = open("06/input.txt", 'r')
lines = f.readlines()
#lines = test_input.split('\n')

line_len = len(lines[0])
num_rows = len(lines)


additions = []
multiplications = []
column_numbes_index = -1
column_numbers = []
multiply = False


for column in range(line_len):
    column_numbers.append("")
    column_numbes_index += 1
    for j in range(num_rows):
        if lines[j][column] == ' ':
            # space can be ignored
            continue
        elif lines[j][column] == '\n':
            # end of line, break out of inner loop
            # this might not be needed
            break
        elif lines[j][column] == '*':
            multiply = True            
        elif lines[j][column] == '+':
            multiply = False
        else:
            # build each number by string concat
            column_numbers[column_numbes_index] += lines[j][column]
            
    print("Column ", column," number: ", column_numbers[column_numbes_index])

    if column_numbers[column_numbes_index].strip() == '':
        print("Processing column numbers: ", column_numbers[:-1], " multiply: ", multiply)
        sum += process_column(column_numbers[:-1], multiply)
        column_numbers = []
        column_numbes_index = -1
        multiply = False

# last column needs to be processed when the input is from variable instead of file
# if from file, this doesn't do anything
sum += process_column(column_numbers, multiply) #should go to IF where we encounter newline

print("Sum: ", sum)

f.close()