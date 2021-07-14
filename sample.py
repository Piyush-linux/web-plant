def add(a,b):
	print(a,"+",b,"=",a+b)
def mul(a,b):
	print(a,"*",b,"=",a*b)
def sqr(a,b):
	print(a,"*",a,"=",a*a,"and",b,"*",b,"=",b*b)
def cub(a,b):
	c=a*a*a
	d=b*b*b
	print("Cube of",a,"is",c,"and",b,"is",d)

x=True
while(x == True):
	x=int(input("Enter value for a : "))
	y=int(input("Enter value for b : "))
	add(x,y)
	mul(x,y)
	sqr(x,y)
	q=input("Do you wanna continue (Y/n) : ")
	if(q == "Y"):
		continue
	else:
		break

