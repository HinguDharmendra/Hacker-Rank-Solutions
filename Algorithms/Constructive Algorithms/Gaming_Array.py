#!/bin/python3

import sys

def play_game(arr, n):
    andy = 0
    bob = 1
    sorted_arr = True
    for index in range(len(arr)-1):
        if arr[index] > arr[index+1]:
            sorted_arr = False
            break
    
    if sorted_arr:
        if n%2 == 1:
            return "BOB"
        else:
            return "ANDY"
    
    while len(arr) > 0:
        if bob:
            max_e = max(arr)
            ind = arr.index(max_e)
            arr = arr[:ind]
            bob = 0
            andy = 1
        else:
            max_e = max(arr)
            ind = arr.index(max_e)
            arr = arr[:ind]
            bob = 1
            andy = 0
    return "BOB" if andy else "ANDY"
            

g = int(input().strip())
for a0 in range(g):
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    print(play_game(arr, n))