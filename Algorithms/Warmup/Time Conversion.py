#!/bin/python

import sys

time = raw_input().strip()
if(time[-2:] == 'PM'):
    temp = int(time.split(':')[0])+12
    if(temp == 24):
        temp = '12'
    else:
        temp = str(temp)
    print temp+time[2:-2]
else:
    if time[:2] == '12':
        temp = '00'
    else:
        temp = time[:2]
    print temp+time[2:-2]