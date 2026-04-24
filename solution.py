print('Ex 4')
import string

sample=[1,2,3,4,'a','b','c','d']
def show():
	string=''
	for a in sample:
		
		string=string+str(a)
	return string


print(f'Sample String: ', show())
def reverse():
	i=0
	j=7
	expected=[0,0,0,0,0,0,0,0]
	for x in sample:
		expected[i]=sample[j]
		j=j-1
		i=i+1
	return expected


def concat():
	string=''
	for x in reverse():
		string=string+str(x)
	return string
print(f'Expected Output: ',concat())


print('Ex 5')
# 3! =1*2*3


def factorial():
	
	reserve=1
	number = 9
	for res in range(9):

		reserve=reserve*number
		number =number-1
	return reserve
print(factorial())

print('ex 7')
def falls(n):
	for i in range(1,10):
		if (n > 1 and n < 10):
			print(f'in range: ', n)
		else:
			print('outside of range')

print(falls(5))
