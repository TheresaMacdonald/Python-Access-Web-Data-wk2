#open a text file, read the numbers, sum the numbers

import re

sum = 0

hand = open('regex_sum_176084.txt') 


for line in hand:
    line = line.rstrip()
    answer = re.findall('[0-9]+', line)
    if not answer:
        continue
    else:
        for ans in answer:
            sum += int(ans)

print(sum)



        
