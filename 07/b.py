

''' This is actually not starting point
test_input = """.......S.......
.......|.......
......|^|......
......|.|......
.....|^|^|.....
.....|.|.|.....
....|^|^|^|....
....|.|.|.|....
...|^|^|||^|...
...|.|.|||.|...
..|^|^|||^|^|..
..|.|.|||.|.|..
.|^|||^||.||^|.
.|.|||.||.||.|.
|^|^|^|^|^|||^|
|.|.|.|.|.|||.|"""
'''

test_input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""


sum = 0

l = []


f = open("07/input.txt", 'r')
lines = f.readlines()
#lines = test_input.split('\n')

arr_lines = []
for line in lines:
    arr_lines.append( list(line) )

# first draw beams
for i in range(1, len(arr_lines)):
    line = arr_lines[i]
    for j, c in enumerate(line):
        above = arr_lines[i-1][j]
        if c == "^":
            arr_lines[i][j-1] = "|" # input doesn't have out of index beams
            arr_lines[i][j+1] = "|"
        elif above == "S" or above == "|":
            arr_lines[i][j] = "|"
        


for line in arr_lines:
    print("".join(line))

print()

# traverse from bottom to top
# assign 1 to each beam at the bottom
# then propagate sums upwards
# at each node, sum left and right beams
# continue propagating the sums upwards
# finally the S node will have the total sum

for row, line in reversed(list(enumerate(arr_lines))):
    for col, c in enumerate(line):
        below = arr_lines[row+1][col] if row+1 < len(arr_lines) else "0"
        if c == "|" and below == "0":
            arr_lines[row][col] = 1
        elif (c == "|" or c == "S") and isinstance(below, int):
            arr_lines[row][col] = below

    for col, c in enumerate(line):
        if c == "^":
            left = arr_lines[row][col-1]
            right = arr_lines[row][col+1]
            node_sum = left + right
            arr_lines[row][col] = node_sum

    # print intermediate state
    #for line in arr_lines:
    #    print("".join( str(x) for x in line))            


for line in arr_lines:
    print("".join( str(x) for x in line))   

f.close()