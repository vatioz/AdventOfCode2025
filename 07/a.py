

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
    #if line.__contains__("^") or line.__contains__("S"):
        arr_lines.append( list(line) )


# first draw beams
#beam_indexes = []
#beam_indexes.append( lines[0].index("S") )

for i in range(1, len(arr_lines)):
    line = arr_lines[i]
    for j, c in enumerate(line):
        above = arr_lines[i-1][j]
        if c == "^" and (above == "S" or above == "|"):
            arr_lines[i][j-1] = "|" # input doesn't have out of index beams
            arr_lines[i][j+1] = "|"
        elif above == "S" or above == "|":
            arr_lines[i][j] = "|"
        


for line in arr_lines:
    print("".join(line))




# after all beams are drawn into the picture, count activated splitters
for i, line in enumerate(arr_lines):
    for j, c in enumerate(line):
        # i = row, j = column
        # c = examined character
        #print(f"Examining {c} at {i},{j}")
        bellow = arr_lines[i+1][j] if i+1 < len(arr_lines) else "."
        if c == "|" and bellow == "^":
            sum += 1


print("Sum: ", sum)
f.close()