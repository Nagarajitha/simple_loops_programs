year = 2020

if year% 400 ==0:
	print('leap year')
elif (year %4 ==0 and year%100 !=0):
	print('leap year')
else:
	print('Not leap year')


# another method

year1 = 2021

if(year1%100 ==0):
	if (year1 %400 == 0):
		print('leap year')
elif(year1 % 4 ==0):
	print('leap year')
else:
	print('not leap year')

# By using Terinary operator

year2 =2020

print('leap year' if (year2%400 or (year2%4==0 and year2 %100!=0 )) else 'not leap year')