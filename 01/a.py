min = 0
max = 99
currentWheelState = 50
zeroLandings = 0

with open("a_input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        direction = line[0]
        amount = int(line[1:])
        # move the wheel
        if direction == "L":
            currentWheelState -= amount
        elif direction == "R":
            currentWheelState += amount

        currentWheelState = currentWheelState % 100
        if currentWheelState == 0:
            zeroLandings += 1

print(zeroLandings)