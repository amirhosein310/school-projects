numberlist = [1,2,2,5,45,58,12,45,86,58,3]
totalodd = 0
for numberodd in numberlist:
	if( numberodd%2 != 0 ):
		totalodd += numberodd
totaleven = 0
for numbereven in numberlist:
	if( numbereven%2 == 0 ):
		totaleven += numbereven

print('total of even numbers are: ',totaleven)
print('toral of odd  numbers are: ',totalodd)

