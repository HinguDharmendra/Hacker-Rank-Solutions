# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function

def gender_wrapper(func):
    def wrap(person):
        func('{title} {firstname} {lastname}'.format(title='Mr.' if person[3] == 'M' else 'Ms.', firstname=person[0], lastname=person[1]))
    
    return wrap

def main():
    N = int(raw_input())
    people = [raw_input().split() for i in range(N)]
    
    gender = gender_wrapper(print)
    for person in sorted(people, key=lambda l: l[2]):
        gender(person)
    
if __name__ == "__main__":
    main()


'''
## Without using decorator
# Enter your code here. Read input from STDIN. Print output to STDOUT
matrix = []
for _ in range(int(raw_input().strip())):
    matrix.append(raw_input().strip().split())

m = sorted(matrix, key=lambda l: l[2])

for row in m:
    if(row[3] == 'M'):
        print 'Mr.', row[0], row[1]
    elif(row[3] == 'F'):
        print 'Ms.', row[0], row[1]   
'''