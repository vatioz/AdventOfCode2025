
test_input = """
3-5
10-14
16-20
12-18
4-4

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
        print("int length: ", len(bounds[0]))
        allBounds.append( (lower, upper) )
    elif line.strip() != '':
        numsToCheck.append(int(line.strip()))
    else:
        continue
    #break

print("All bounds: ", len(allBounds))


print("Starting checks")
ingredientSet = set()
for i, bound in enumerate(allBounds):
    #print(allBounds)
    lowerBound =  bound[0]
    upperBound = bound[1]
    for j in range(i+1, len(allBounds)):
        followingBound = allBounds[j]
        followingLow = followingBound[0]
        followingHigh = followingBound[1]
        if upperBound < followingLow or lowerBound > followingHigh :
            continue # no overlap
        elif lowerBound < followingLow and upperBound >= followingLow and upperBound <= followingHigh:
            allBounds[j] = (lowerBound, followingHigh)
            allBounds[i] = (0, 0) # mark as reused
            #print("Merging up ", bound, " with\n            ", followingBound, " into ", allBounds[j])
            break
        elif lowerBound >= followingLow and lowerBound <= followingHigh and upperBound > followingHigh:
            allBounds[j] = (followingLow, upperBound)
            allBounds[i] = (0, 0) # mark as reused
            #print("Merging dn ", bound, " with\n              ", followingBound, " into ", allBounds[j])
            break
        elif lowerBound >= followingLow and upperBound <= followingHigh:
            allBounds[i] = (0, 0) # mark as reused
            break
        elif lowerBound < followingLow and upperBound > followingHigh:
            allBounds[j] = (lowerBound, upperBound)
            allBounds[i] = (0, 0) # mark as reused
            break

freshIngredients = 0
#print("Merged bounds: ", allBounds)
for bound in allBounds:
    if(bound == (0,0)):
        continue
    print("Counting bound: ", bound)
    low = bound[0]
    high = bound[1]
    freshIdsInBound = (high - low + 1)
    print("  Fresh IDs in bound: ", freshIdsInBound)
    freshIngredients += freshIdsInBound
        

print("Fresh ingredients: ", freshIngredients)
            

f.close()