# Enter your code here. Read input from STDIN. Print output to STDOUT
c, d=[complex(*map(float,raw_input().split())) for i in range(2)]

def myPrint(c):
	output=''
	if c.real: output+='%.2f'%c.real
	if c.imag:
		if c.real:
			output+=('-' if c.imag<0 else '+')+'%.2fi'%abs(c.imag)
		else:
			output+='0.00'+('-' if c.imag<0 else '+')+'%.2fi'%abs(c.imag)
	else:
		if c.real:
			output+=('-' if c.imag<0 else '+')+'0.00i'
		else:
			output+='0.00+0.00i'
	print output

myPrint(c+d)
myPrint(c-d)
myPrint(c*d)
myPrint(c/d)
myPrint(abs(c))
myPrint(abs(d))