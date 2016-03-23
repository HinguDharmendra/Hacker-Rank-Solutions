# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

k = int(raw_input().strip())
roomNumberList = map(int, raw_input().split())

c = collections.Counter()
for roomNumber in roomNumberList:
    c[roomNumber]+=1

for roomNumber in roomNumberList:
    if(c[roomNumber] == 1):
        print roomNumber
        break

'''
### This is correct solution but gives timing out
distinctRoomNumbers = set(roomNumberList)
for roomNumber in distinctRoomNumbers:
    if(roomNumberList.count(roomNumber) == 1):
        print roomNumber
'''