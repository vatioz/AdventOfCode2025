
test_input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""



freshIngredients = 0

allBounds = []
numsToCheck = []

f = open("05/input.txt", 'r')
lines = f.readlines()
#lines = test_input.split('\n')



for line in lines:
    #print("Line: ", line)
    if(line.__contains__('-')):
        #first part
        bounds = line.split('-')
        lower = int(bounds[0])
        upper = int(bounds[1])
        allBounds.append( (lower, upper) )
    elif line.strip() != '':
        numsToCheck.append(int(line.strip()))
    else:
        continue

print("Starting checks")
for num in numsToCheck:
    for bound in allBounds:
        if bound[0] <= num <= bound[1]:
            freshIngredients += 1
            print("Fresh: ", num)
            break


print("Fresh ingredients: ", freshIngredients)
            

f.close()