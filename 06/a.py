


test_input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + """



sum = 0

rows = []
results = []

f = open("06/input.txt", 'r')
lines = f.readlines()
#lines = test_input.split('\n')

for line in lines:
    print("Line: ", line)
    parts = line.split(' ')
    print("Parts: ", parts)
    row = []
    for part in parts:
        if(part.strip() == ''):
            continue
        part = part.strip()
        row.append(part)
    rows.append(row)

operations = rows[-1]
len_rows = len(rows)-1
len_cols = len(rows[0])

print("Len rows: ", len_rows, " len cols: ", len_cols)

for i in range(len_cols):
    column_result = int(rows[0][i])
    for j in range(1, len_rows):
        op = operations[i].strip()
        print("Processing col ", i, " row ", j, " op ", op, " val ", rows[j][i])
        if(op == '*'):
            print("Multiplying ", column_result, " by ", int(rows[j][i]))
            column_result *= int(rows[j][i])
            print("Intermediate result: ", column_result)
        elif(op == '+'):
            print("Adding ", int(rows[j][i]), " to ", column_result)
            column_result += int(rows[j][i])
            print("Intermediate result: ", column_result)
    results.append(column_result)

for res in results:
    sum += res

print("Sum: ", sum)
f.close()