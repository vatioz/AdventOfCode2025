
test_input = """987654321111111
811111111111119
234234234234278
818181911112111"""

bank_joltages = []

with open("03/input.txt") as f:
    lines = f.readlines()
    for battery_bank in lines:
        battery_bank = battery_bank.strip()
    #for battery_bank in test_input.splitlines():
        print("Battery bank:", battery_bank)
        joltages = []
        left_highest = 0
        right_highest = 0
        for c in battery_bank:
            joltage = int(c)

            if right_highest > left_highest: # always move higher to left and put whatever to right
                left_highest = right_highest
                right_highest = joltage
                continue

            # if joltage > left_highest and right_highest > left_highest:
            #     left_highest = right_highest
            #     right_highest = joltage
            
            
            elif joltage > right_highest:            
                right_highest = joltage

            
        bank_joltage = f"{left_highest}{right_highest}"
        bank_joltages.append(int(bank_joltage))
        print("Bank joltage:", bank_joltage)
        
total_joltage = sum(bank_joltages) 
print("Total joltage:", total_joltage)

