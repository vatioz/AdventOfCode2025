
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
        #print("Battery bank:", battery_bank)
        joltages = []
        queue = []
        for c in battery_bank:
            popped = False
            joltage = int(c)
            #print("Current queue:", queue)

            if len(queue) < 12:
                queue.append(joltage)
                continue
                

            for i in range(len(queue)-1):
                left = i
                right = i+1
                if(queue[right] > queue[left]):
                    queue.pop(left)
                    queue.append(joltage)
                    popped = True
                    break
                
            if popped:
                continue

            if joltage > queue[11]:                
                queue[11] = joltage
                continue
                
        #print("Current queue:", queue)
            

        
        bank_joltage = ''.join(str(x) for x in queue)
        bank_joltages.append(int(bank_joltage))
        #print("Bank joltage:", bank_joltage)
        
total_joltage = sum(bank_joltages) 
print("Total joltage:", total_joltage)


