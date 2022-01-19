s=input('input string''\n')
lastch= input('enter last character''\n')
exception = input('enter exception''\n')
x = s.split(lastch)
splitstring = x[0]
#print(splitstring)
num_exception = splitstring.count(exception)
#print(num_exception)
num_letters = sum(c.isalpha() for c in splitstring)
num_finalstring = num_letters - num_exception
print(num_finalstring)



