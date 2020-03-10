import sys

digit_string = sys.argv[1]
sum = 0
for number in digit_string:
    sum = sum + int(number)
print(sum)