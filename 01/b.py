# create basic structure for a basic class without any context, but with constructor, one method and class property

class WheelClicker:
    class_property = "I am a class property"
    currentWheelState = 0
    zeroPassings = 0

    def __init__(self, value):
        self.currentWheelState = value

    def rotate_left(self, amount):
        for _ in range(amount):
            self.currentWheelState -= 1
            if self.currentWheelState == 0:
                self.zeroPassings += 1
            if self.currentWheelState < 0:
                self.currentWheelState = 99
        

    def rotate_right(self, amount):
        for _ in range(amount):
            self.currentWheelState += 1
            if self.currentWheelState == 100:
                self.zeroPassings += 1
                self.currentWheelState = 0
    
    def print_status(self):
        print(f"Current Wheel State: {self.currentWheelState}, Zero Passings: {self.zeroPassings}")


currentWheelState = 50

wheel = WheelClicker(currentWheelState)

with open("a_input_test.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        direction = line[0]
        amount = int(line[1:])
        
        # move the wheel
        wheel.rotate_left(amount) if direction == "L" else wheel.rotate_right(amount)

wheel.print_status()