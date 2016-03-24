# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils

for _ in range(int(raw_input())):
    tuple = email.utils.parseaddr(raw_input())              #or name, email = raw_input().split()
                                                            #email = email[1:-1]
    #result = re.findall(r'[\w\.-\_]+@[\w\.-\_]+', email)   #Passes the basic email validation
    
    result = re.findall(r'(^[a-z][\w\_\.-]+)@([a-z]+)\.([a-z]{1,3}$)', tuple[1], re.IGNORECASE)# instead of tuple[1] use email
    #print result
    if(bool(result)):
        print email.utils.formataddr(tuple) # or name+" <"+email+">"