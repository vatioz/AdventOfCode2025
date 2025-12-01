min = 0
max = 99
currentWheelState = 50
zeroLandings = 0

directionsMap = {
    "L": -1,
    "R": 1
}

with open("a_input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        direction = line[0]
        amount = int(line[1:])
        
        # move the wheel
        currentWheelState += directionsMap[direction] * amount

        currentWheelState = currentWheelState % 100
        if currentWheelState == 0:
            zeroLandings += 1

print(zeroLandings) # correct answer is 1034