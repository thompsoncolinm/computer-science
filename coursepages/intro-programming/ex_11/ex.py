import re

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "regex_sum_42.txt"
handle = open(fname)
# use re.findall() to find all numbers in the file
#add all the numbers together
# print the sum of the numbers
sum = 0
for line in handle:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        sum += int(number)
print(sum)