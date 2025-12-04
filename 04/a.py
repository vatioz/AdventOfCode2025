
test_input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


sumOfReachable = 0



rows = []

f = open("04/input.txt", 'r')
lines = f.readlines()
#lines = test_input.split('\n')

row_length = len(lines[0].strip())
rows.append([0]*(row_length+2))

for line in lines:
    line = line.strip()
    line = line.replace('.', '0')
    line = line.replace('@', '1')
    line = '0' + line + '0'
    row = list(line)
    rows.append(row)
    

rows.append([0]*(row_length+2))

for i in range(1, len(rows)-1):
    for j in range(1, len(rows[i])-1):
        print(rows[i][j], end='')
        if(rows[i][j] == '0'):
            continue
        sumForRoll = 0

        sumForRoll += int(rows[i-1][j-1])
        sumForRoll += int(rows[i-1][j])
        sumForRoll += int(rows[i-1][j+1])

        sumForRoll += int(rows[i][j-1])
        #sum += rows[i][j]
        sumForRoll += int(rows[i][j+1])
        
        
        sumForRoll += int(rows[i+1][j-1])
        sumForRoll += int(rows[i+1][j])
        sumForRoll += int(rows[i+1][j+1])

        if sumForRoll < 4:
            sumOfReachable += 1
            #print("* ", end='')

    print("\nSum for line: ", sumOfReachable)

    

print("\nFinal sum: ", sumOfReachable)
    


f.close()