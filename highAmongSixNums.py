a,b,c,d,e,f = 1,2,8,4,5,6

if(a>b and a>c and a>d and a>e and a>f):
	print('a is highest')
elif(b>c and b>d and b>e and b>f):
	print('b is highest')
elif(c>d and c>e and c>f):
	print('c is highest')
elif (d>e and d>f):
	print('d is highest')
elif(e>f):
	print('e is highest')
else:
	print('f is highest')