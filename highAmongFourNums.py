a,b,c,d = 45,50,40,11

if (a>b):
	if(a>c):
		if(a>d):
			print('a is highest')
		else:
			print('d is highest')
	else:
		if (c>d):
			print('c id highest')
		else:
			print('d is highest')
else:
	if(b>c):
		if(b>d):
			print('b is highest')
		else:
			print('d is highest')
	else:
		if (c>d):
			print('c is highest')
		else:
			print('d is highest')