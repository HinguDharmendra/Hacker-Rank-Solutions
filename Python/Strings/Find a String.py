# Enter your code here. Read input from STDIN. Print output to STDOUT

string = raw_input()
substring = raw_input()

count = 0
found=False
if((substring in string) and (len(string)>len(substring)) and (len(string)>=1 and len(string)<=200)):
    #print string.count(substring) ###Gives faulty result for this scenario
    for i in range(len(string)):
        if string[i:].startswith(substring):
            count+=1
print count    
            
            