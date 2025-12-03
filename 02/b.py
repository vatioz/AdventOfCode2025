
invalid_ids = []
with open("02/input.txt", "r") as input:
    text = input.read().strip()
    ranges = text.split(',')
    for block in ranges:
        print(block)
        range_parts = block.split("-")
        start = int(range_parts[0])
        end = int(range_parts[1])
        print(f"start: {start}, end: {end}")
        for num in range(start, end + 1):
            num_str = str(num) 
            length = len(num_str)
            half_len = length // 2
            for chunk_size in range(1, half_len + 1):
                if(length % chunk_size != 0):
                    #print(f"Skipping chunk size {chunk_size} for number {num} since it doesn't divide evenly.")
                    continue
                how_many_chunks = length // chunk_size                
                #print(f"Number: {num}, Length: {length}, half_len: {half_len}, Chunk size: {chunk_size}, How many chunks: {how_many_chunks}")
                chunks = []
                start = 0
                for attempt in range(how_many_chunks):
                    chunk = num_str[start: start + chunk_size]
                    start += chunk_size
                    chunks.append(chunk)
                deduped_chunks = set(chunks)
                if(len(deduped_chunks) == 1):
                    print(f"!!! Invalid ID found: {num} All chunks are the same for chunk size {chunk_size}! Chunks: {chunks}")
                    invalid_ids.append(num) 
                    break # no need to check other chunk sizes

sum = sum(invalid_ids)
#print("Invalid IDs:", invalid_ids)
print("Sum of invalid IDs:", sum)








#print("Chunks:", chunks)

# part1 = num[0:3]
# part2 = num[3:6]
# part3 = num[6:9]

# print(part1, part2, part3)