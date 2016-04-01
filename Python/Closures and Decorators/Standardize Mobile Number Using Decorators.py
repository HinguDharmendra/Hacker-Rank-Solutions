# Enter your code here. Read input from STDIN. Print output to STDOUT

number = []
for i in range(int(raw_input().strip())):
    number.append(raw_input().strip())

def mobile(function):
    def input(number):
            return sorted([function(i) for i in number])
    return input

@mobile
def standardize(number):
	return '+91' + ' ' + number[-10:-5] + ' ' + number[-5:]

print '\n'.join(standardize(number))

'''
## Without using decorators
# Enter your code here. Read input from STDIN. Print output to STDOUT
mobile_numbers = []
for _ in range(int(raw_input().strip())):
    mobile_numbers.append(raw_input().strip()[-10:])

sortedNumbers = sorted(mobile_numbers)
for number in sortedNumbers:
    print "{prefix} {left} {right}".format(prefix = '+91', left = number[-10:-5], right = number[-5:])
'''